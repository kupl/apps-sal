import random
t = int(input())
while t > 0:
    t -= 1

    n, k, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    temp = list(range(n, 0, -1))
    random.shuffle(temp)
    # random.shuffle(temp)
    ans = [str(i) for i in temp]
    print(' '.join(ans[::-1]))
