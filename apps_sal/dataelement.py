from pathlib import Path
from typing import Dict
from typing import Iterable
from typing import Union
import json
import logging


class DataElement:

    def __init__(self, path: Union[str, Path]) -> None:
        # Base directory
        self.path: Path = Path(path)

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
            logging.warning(f'No such file: "{input_output_json}"')

        # Load solutions
        self.solutions: Iterable[str] = []
        solutions_dir = self.path / 'solutions'
        if solutions_dir.exists():
            self.solutions = [py.read_text() for py in solutions_dir.glob('*.py')]

    def __repr__(self) -> str:
        return f'DataElement("{self.path}")'

    def score(self, program: str) -> float:
        raise NotImplementedError(
            'app_sal.dataelement.DataElement.score is not implemeted.')
