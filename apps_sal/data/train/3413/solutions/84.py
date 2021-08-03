import pandas as pd


def solution(nums):
    df = pd.DataFrame()
    df['S'] = nums
    answer = list(df['S'].sort_values().values)
    print(list(answer))
    return answer
