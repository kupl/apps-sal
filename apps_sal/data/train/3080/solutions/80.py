from typing import List


def who_is_paying(name: str) -> List[str]:
    return [name, name[0:2]] if len(name) > 2 else [name]
