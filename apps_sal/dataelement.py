from pathlib import Path
from typing import Dict
from typing import List
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
        self.solutions: List[str] = []
        solutions_json = self.path / 'solutions.json'
        if solutions_json.exists():
            with solutions_json.open() as f:
                self.solutions = json.load(f)

    def __repr__(self) -> str:
        return f'DataElement("{self.path}")'
