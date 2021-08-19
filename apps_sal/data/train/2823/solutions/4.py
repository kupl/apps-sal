from typing import List, Union


def duplicates(array: List[Union[int, str]]) -> List[Union[int, str]]:
    (d, res) = ({}, [])
    for a in array:
        if d.setdefault(a, 0) == 1:
            res.append(a)
        d[a] += 1
    return res
