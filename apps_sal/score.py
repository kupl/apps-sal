from __future__ import annotations
from io import StringIO
from itertools import chain
from typing import Callable
from typing import Dict
from typing import Union
from unittest.mock import mock_open
from unittest.mock import patch
import multiprocessing as mp
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


def score_stdio_exact(pgm: str, in_out: Dict[str, str], timeout: Union[None, int] = None) -> float:

    try:
        # test for each io
        results = []
        for input, expected in zip(in_out['inputs'], in_out['outputs']):

            try:
                # run program
                with mp.Pool(processes=1) as pool:
                    output = pool.apply_async(run_stdio, (pgm, input))
                    output = output.get(timeout)

                # recored result
                results.append(expected.strip() == output.strip())
            except Exception as exception:
                if isinstance(exception, mp.TimeoutError):
                    get_logger().warning('Timeout while evaluating program.')
                results.append(False)

        score = sum(results) / len(results)
    except Exception:
        score = 0.0
    return score
