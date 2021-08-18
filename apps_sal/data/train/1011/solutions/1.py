t = int(input())


def do():
    n, k = list(map(int, input().split()))
    s = input()
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    if lower > k and upper <= k:
        print('chef')
    elif(upper > k and lower <= k):
        print('brother')
    elif(upper <= k and lower <= k):
        print('both')
    else:
        print('none')
    return


for i in range(t):
    do()
