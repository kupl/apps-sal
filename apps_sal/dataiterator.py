from typing import List

from apps_sal.dataelement import DataElement


class DataIterator:

    def __init__(self, data: List[DataElement]) -> None:
        self.data: List[DataElement] = list(data)
        self.index: int = 0

    def __len__(self) -> int:
        return len(self.data)

    def __next__(self) -> DataElement:
        if self.index >= len(self.data):
            raise StopIteration
        current = self.data[self.index]
        self.index += 1
        return current
