from typing import List

def sorter(textbooks: List[str]) -> List[str]:
    """Returns the textbooks non-case-sensitive sorted."""
    return sorted(textbooks, key=str.casefold)
