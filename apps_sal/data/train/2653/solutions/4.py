def bingo(array): 
    return ["LOSE", "WIN"][{2, 7, 9, 14, 15} <= set(array)]
