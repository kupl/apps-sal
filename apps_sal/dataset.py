from __future__ import annotations

from pathlib import Path
from typing import List
from typing import Union

from apps_sal.dataelement import DataElement
from apps_sal.dataiterator import DataIterator


class Dataset:

    def __init__(self, path: Union[str, Path]) -> None:
        self.path: Path = Path(path)
        self.data: List[DataElement] = list(
            map(DataElement, self.path.glob('*')))
        self.index: int = 0

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> DataIterator:
        return DataIterator(self.data)

    def __repr__(self) -> str:
        return f'Dataset("{self.path.name}")'

    def __getitem__(self, idx: int) -> DataElement:
        return self.data[idx]


def load_dataset(path: Union[str, Path]) -> Dataset:
    return Dataset(path)


def load_train_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset(filepath / 'data/train')


def load_test_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset(filepath / 'data/test')
