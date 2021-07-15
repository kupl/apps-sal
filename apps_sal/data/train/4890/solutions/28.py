from typing import List

def find_difference(a: List[int], b: List[int]) -> int:
    mult3 = lambda x: x[0]*x[1]*x[2]
    return abs( mult3(a)-mult3(b) )
