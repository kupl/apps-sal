def loneliest(number):
    seq = list(map(int, str(number)))
    temp = 0
    ans = 100
    ans1 = 100
    key = 0
    x = 0
    if seq.count(1) == 0:
        return False
    for i in seq:
        temp = sum(seq[x + 1:x + i + 1]) + sum(seq[x - i if x > i else 0:x])
        if i == 1:
            if temp < ans1:
                ans1 = temp
        elif temp < ans:
            ans = temp
        x += 1
    if ans1 <= ans:
        return True
    else:
        return False
