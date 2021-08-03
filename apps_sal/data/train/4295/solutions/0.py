def balancedNum(n):
    s = str(n)
    l = (len(s) - 1) // 2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"


balanced_num = balancedNum
