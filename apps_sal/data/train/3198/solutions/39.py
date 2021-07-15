from typing import List

def check_exam(arr1: List[str], arr2: List[str]) -> int:
    """ Get the score of the exam based on correct answers and student's answers. """
    _exam_points_sum = sum([0 if not _it[1] else 4 if _it[0] == _it[1] else -1 for _it in zip(arr1, arr2)])
    return _exam_points_sum if _exam_points_sum > 0 else 0
