from __future__ import annotations
from pathlib import Path
from typing import Dict
from typing import Iterable
from typing import List
from typing import Union
import json

from apps_sal.logger import get_logger
from apps_sal.score import score_stdio_exact


class DataElement:

    def __init__(self, path: Union[str, Path]) -> None:
        # Base directory
        self.path: Path = Path(path)
        self.id: str = self.path.name

        # Load natural language question
        with (self.path / 'question.txt').open() as f:
            self.text: str = f.read()

        # Load metadata
        with (self.path / 'metadata.json').open() as f:
            self.metadata: Dict[str, str] = json.load(f)

        # Load input output examples
        self.input_output: Dict[str, str] = {}
        input_output_json = self.path / 'input_output.json'
        if input_output_json.exists():
            with input_output_json.open() as f:
                self.input_output = json.load(f)
        else:
            get_logger().warning(f'No such file: "{input_output_json}"')

        # Load solutions
        self.solutions: Iterable[str] = []
        solutions_dir = self.path / 'solutions'
        if solutions_dir.exists():
            self.solutions = [py.read_text() for py in solutions_dir.glob('*.py')]
        
        # Load starter code
        starter_code_py = self.path / 'starter_code.py'
        if starter_code_py.exists():
            with starter_code_py.open() as f:
                self.starter_code = starter_code_py.read_text()

    def __repr__(self) -> str:
        return f'DataElement("{self.path}")'

    def load_per_program(self) -> List[DataElement]:
        elements = []
        if len(self.solutions) == 0:
            get_logger().warning(f'This problem is discarded since it does not have any reference solution: {self.path}')
        for solution in self.solutions:
            element = DataElementPerProgram(self.path, self.text, self.metadata, self.input_output, solution, self.starter_code)
            elements.append(element)
        return elements

    def to_json(self, with_solutions=True, with_input_output=False, with_metadata=False, with_starter_code=True) -> str:
        data = {}
        data['id'] = self.id
        data['text'] = self.text
        if with_solutions:
            data['solutions'] = self.solutions
        if with_input_output:
            data['input_output'] = self.input_output
        if with_metadata:
            data['path'] = str(self.path)
            data['metadata'] = self.metadata
        if with_starter_code:
            data['starter_code'] = self.starter_code
        return json.dumps(data)

    def score(self, program: str, timeout: Union[None, int] = None, processes: Union[int, None] = None) -> float:
        if not ('stdio' in self.metadata['types'] and 'exact' in self.metadata['types']):
            get_logger().warning('Problem without "stdio" and "exact" tags. This may consider your program wrong even if it is correct.')
        return score_stdio_exact(program, self.input_output, timeout=timeout, processes=processes)


class DataElementPerProgram(DataElement):

    # pylint: disable=super-init-not-called
    def __init__(self, path: Union[str, Path], text: str, metadata: Dict[str, str], io: Dict[str, str], solution: str, starter_code: str) -> None:
        self.path: Path = Path(path)
        self.id: str = self.path.name
        self.text: str = text
        self.metadata: Dict[str, str] = metadata
        self.input_output: Dict[str, str] = io
        self.solution: str = solution
        self.solutions: List[str] = [self.solution]
        self.starter_code = starter_code

    def to_json(self, with_solutions=True, with_input_output=False, with_metadata=False, with_starter_code=True) -> str:
        data = {'text': self.text}
        if with_solutions:
            data['solution'] = self.solution
        if with_input_output:
            data['input_output'] = self.input_output
        if with_metadata:
            data['path'] = str(self.path)
            data['metadata'] = self.metadata
        if with_starter_code:
            data['starter_code'] = self.starter_code
        return json.dumps(data)

    def __repr__(self) -> str:
        return f'DataElementPerProgram("{self.path}")'
