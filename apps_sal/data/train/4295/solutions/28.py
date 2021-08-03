def balanced_num(n):
    lst = [int(i) for i in str(n)]
    return "Balanced" if sum(lst[:int(((len(lst) - 1) / 2))]) == sum(lst[int(((len(lst) + 2) / 2)):]) else "Not Balanced"
