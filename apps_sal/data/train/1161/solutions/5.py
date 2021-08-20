T = int(input())
for i in range(T):
    S = str(input())
    c = S.count('s')
    d = S.count('m')
    j = 0
    while j < len(S) - 1:
        if S[j] == 's' and S[j + 1] == 'm' or (S[j] == 'm' and S[j + 1] == 's'):
            j += 2
            c -= 1
        else:
            j += 1
    if c > d:
        print('snakes')
    elif d > c:
        print('mongooses')
    else:
        print('tie')
