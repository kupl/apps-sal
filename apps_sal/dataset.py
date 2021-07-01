from __future__ import annotations

from pathlib import Path
from typing import List
from typing import Union

from apps_sal.dataelement import DataElement
from apps_sal.dataiterator import DataIterator

class Dataset:

    def __init__(self, path: Union[str, Path], shuffle: bool=False) -> None:
        self.path: Path = Path(path)
        self.data: List[DataElement] = list(map(DataElement, self.path.glob('*')))
        self.shuffle: bool = shuffle
        self.index: int = 0

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> DataIterator:
        return DataIterator(self.data, self.shuffle)

    def __repr__(self) -> str:
        return f'Dataset("{self.path}")'

def load_dataset(path: Union[str, Path]) -> Dataset:
    return Dataset(path)
