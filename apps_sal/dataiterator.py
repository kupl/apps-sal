from typing import List
import random

from apps_sal.dataelement import DataElement

class DataIterator:

    def __init__(self, data: List[DataElement], shuffle: bool=False) -> None:
        self.data: List[DataElement] = list(data)
        if shuffle:
            random.shuffle(self.data)
        self.index: int = 0

    def __len__(self) -> int:
        return len(self.list)

    def __next__(self) -> DataElement:
        if self.index >= len(self.list):
            raise StopIteration
        current = self.data[self.index]
        self.index += 1
        return current
