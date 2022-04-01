from __future__ import annotations
from functools import partial
from io import StringIO
from itertools import chain
from multiprocessing.connection import Connection
from multiprocessing.pool import ThreadPool
from typing import Callable
from typing import Dict
from typing import Tuple
from typing import Union
from unittest.mock import mock_open
from unittest.mock import patch
import contextlib
import multiprocessing as mp
import signal
import types

from apps_sal.logger import get_logger


def make_stdio_runnable(pgm: str) -> Callable[[], None]:
    # append function wrapper
    pgm = pgm.splitlines()
    pgm = map(lambda line: '\t' + line, pgm)
    pgm = '\n'.join(chain(['def code():'], pgm))

    # create module
    module = types.ModuleType('test_program', '')
    module.__file__ = '<runtime_module>'

    # evaluate the given program
    g = {}
    exec(pgm, g)
    module.__dict__.update(g)

    return getattr(module, 'code')


def run_stdio(pgm: str, input: str) -> str:

    # make callable program
    pgm = make_stdio_runnable(pgm)

    stdout = StringIO()

    @patch('builtins.open', mock_open(read_data=input))
    @patch('sys.stdin', StringIO(input))
    @patch('sys.stdout', stdout)
    def _inner_run_stdio(_pgm):
        try:
            _pgm()
        except SystemExit:
            pass

    _inner_run_stdio(pgm)
    return stdout.getvalue()


class TimeoutExcpetion(Exception):
    pass


@contextlib.contextmanager
def time_limit(seconds: float):
    if seconds is None:
        yield

    else:
        def signal_handler(*_):
            raise TimeoutExcpetion()
        signal.setitimer(signal.ITIMER_REAL, seconds)
        signal.signal(signal.SIGALRM, signal_handler)
        try:
            yield
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)


def _score_stdio_exact_aux_with_timeout(timeout: int, args: Tuple[str, str, str]) -> bool:
    receive_end, send_end = mp.Pipe(duplex=False)
    p = mp.Process(target=_score_stdio_exact_aux, args=[args], kwargs=dict(send_end=send_end))
    p.daemon = True
    p.start()
    send_end.close()
    p.join(timeout)
    if p.is_alive():
        get_logger().warning('Timeout while evaluating program.')
        p.terminate()
        return False
    else:
        return receive_end.recv()


def _score_stdio_exact_aux(args: Tuple[str, str, str], send_end: Connection = None) -> bool:
    pgm, input, expected = args
    result = False
    try:
        output = run_stdio(pgm, input)
        result = expected.strip() == output.strip()
    except Exception:
        pass
    if send_end is not None:
        send_end.send(result)
    else:
        return result


def score_stdio_exact(pgm: str, in_out: Dict[str, str], timeout: Union[int, None] = None, processes: Union[int, None] = None) -> float:

    def make_args(in_exp: Tuple[str, str]) -> Tuple[str, str, str]:
        input, expected = in_exp
        return pgm, input, expected
    args = map(make_args, zip(in_out['inputs'], in_out['outputs']))

    try:
        score = 0
        num = 0
        with ThreadPool(processes=processes) as pool:
            func = partial(_score_stdio_exact_aux_with_timeout, timeout) if timeout is not None else _score_stdio_exact_aux
            for result in pool.imap_unordered(func, args):
                score += result
                num += 1
        score = score / num
    except Exception:
        score = 0.0
    return score
