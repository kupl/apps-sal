from __future__ import annotations

from pathlib import Path
from typing import Callable
from typing import List
from typing import Union

from apps_sal.dataelement import DataElement
from apps_sal.dataiterator import DataIterator


class Dataset:

    def __init__(self, data: List[DataElement], name: Union[None, str] = None) -> None:
        self.name: str = name if name is not None else 'APPS-SAL'
        self.data: List[DataElement] = data

    @classmethod
    def from_path(cls, path: Union[str, Path]) -> Dataset:
        path = Path(path)
        data = [DataElement(p) for p in path.glob('*') if not p.name.endswith('buggy')]
        return Dataset(data, str(path))

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> DataIterator:
        return DataIterator(self.data)

    def __repr__(self) -> str:
        return f'Dataset("{self.name}")'

    def __getitem__(self, idx: int) -> DataElement:
        return self.data[idx]

    def filter(self, filtering_function: Callable[[DataElement], bool]) -> Dataset:
        data = [elem for elem in self.data if filtering_function(elem)]
        return Dataset(data, self.name)

    def map(self, mapping_function: Callable[[DataElement], DataElement]) -> Dataset:
        data = [mapping_function(elem) for elem in self.data]
        return Dataset(data, self.name)

    def load_per_program(self) -> Dataset:
        data = sum((elem.load_per_program() for elem in self.data), [])
        return Dataset(data, self.name)

    def to_jsonl(self, *args, **kwargs) -> str:
        return '\n'.join((elem.to_json(*args, **kwargs) for elem in self.data))

    def query(self, id: Union[int, str]) -> Union[DataElement, None]:
        if not isinstance(id, str):
            id = f'{id:04d}'
        for elem in self.data:
            if str(elem.path).endswith(id):
                return elem
        return None


def load_dataset_from_path(path: Union[str, Path]) -> Dataset:
    return Dataset.from_path(path)


def load_train_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset_from_path(filepath / 'data/train')


def load_test_dataset() -> Dataset:
    filepath = Path(__file__).parent
    return load_dataset_from_path(filepath / 'data/test')
