from __future__ import annotations

from pathlib import Path
from typing import Callable
from typing import List
from typing import Union

from apps_sal.dataelement import DataElement
from apps_sal.dataiterator import DataIterator


class Dataset:

    def __init__(self, path: Union[str, Path]) -> None:
        self.path: Path = Path(path)
        self.data: List[DataElement] = [DataElement(p) for p in self.path.glob('*')]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> DataIterator:
        return DataIterator(self.data)

    def __repr__(self) -> str:
        return f'Dataset("{self.path.name}")'

    def __getitem__(self, idx: int) -> DataElement:
        return self.data[idx]

    def filter(self, filtering_function: Callable[[DataElement], bool]) -> Dataset:
        self.data = [elem for elem in self.data if filtering_function(elem)]
        return self

    def map(self, mapping_function: Callable[[DataElement], DataElement]) -> Dataset:
        self.data = [mapping_function(elem) for elem in self.data]
        return self


def load_dataset(path: Union[str, Path]) -> Dataset:
    return Dataset(path)


def load_train_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset(filepath / 'data/train')


def load_test_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset(filepath / 'data/test')
