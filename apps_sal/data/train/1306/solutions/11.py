def possible(s):
    for i in "LTIM":
        if s.count(i) < 2:
            return False

    if len(s) == 9:
        if s.count('E') < 1:
            return False
    else:
        if s.count('E') < 2:
            return False

    return True


for T in range(int(input())):
    S = input()

    if possible(S):
        print('YES')
    else:
        print('NO')
