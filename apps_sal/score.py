from __future__ import annotations
from io import StringIO
from itertools import chain
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


def _score_stdio_exact_aux(args: Tuple[str, str, str, Union[int, None]]) -> bool:
    pgm, input, expected, timeout = args
    result = False

    try:
        with time_limit(timeout):
            output = run_stdio(pgm, input)
        result = expected.strip() == output.strip()
    except Exception as exception:
        if isinstance(exception, TimeoutExcpetion):
            get_logger().warning('Timeout while evaluating program.')
        result = False
    return result


def score_stdio_exact(pgm: str, in_out: Dict[str, str], timeout: Union[None, int] = None, processes: Union[int, None] = None) -> float:

    def make_args(in_exp: Tuple[str, str]) -> Tuple[str, str, str, Union[int, None]]:
        input, expected = in_exp
        return pgm, input, expected, timeout
    args = map(make_args, zip(in_out['inputs'], in_out['outputs']))

    try:
        with mp.Pool(processes) as pool:
            results = pool.map(_score_stdio_exact_aux, args)
        score = sum(results) / len(results)
    except Exception:
        score = 0.0
    return score
