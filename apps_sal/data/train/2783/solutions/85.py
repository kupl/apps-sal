import numpy as np

def get_grade(*scores):
    grades = {10: 'A', 9:'A', 8:'B', 7:'C', 6:'D'}
    return grades.get(np.mean(scores) // 10, 'F')
