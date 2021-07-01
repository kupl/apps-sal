from pathlib import Path
from typing import Union
from typing import List

class DataElement:

    def __init__(self, path: Union[str, Path]) -> None:
        self.path: Path = Path(path)
        