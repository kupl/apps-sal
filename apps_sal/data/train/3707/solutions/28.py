from typing import List

def sorter(textbooks: List[str]) -> List[str]:
    """Returns the textbooks list non-case-sensitive sorted."""
    return sorted(textbooks, key=str.lower)
