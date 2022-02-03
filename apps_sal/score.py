from __future__ import annotations
from io import StringIO
from itertools import chain
from typing import Callable
from typing import Dict
from unittest.mock import patch
import types


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


def run_stdio(pgm: Callable[[], None], input: str) -> str:

    stdout = StringIO()

    @patch('sys.stdin', StringIO(input))
    @patch('sys.stdout', stdout)
    def _inner_run_stdio(_pgm):
        try:
            _pgm()
        except SystemExit:
            pass

    _inner_run_stdio(pgm)
    return stdout.getvalue()


def score_stdio_exact(pgm: str, in_out: Dict[str, str]) -> float:

    # make callable program
    pgm = make_stdio_runnable(pgm)

    # test for each io
    results = []
    for input, expected in zip(in_out['inputs'], in_out['outputs']):

        # run program
        output = run_stdio(pgm, input)

        # recored result
        results.append(expected.strip() == output.strip())

    score = sum(results) / len(results)
    return score
