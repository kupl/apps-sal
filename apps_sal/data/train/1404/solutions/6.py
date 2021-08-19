for i in range(eval(input())):
    l = list(map(int, input().split()))
    l.sort()
    b = set(l)
    k1 = eval(input())
    answer = 0
    if k1 <= l[0] + 1:
        answer += 1 + 3 * (k1 - 1)
        print(answer)
    elif k1 <= l[1] + 1:
        answer += 1 + 3 * l[0]
        k1 -= l[0]
        answer += 2 * (k1 - 1)
        print(answer)
    else:
        answer += 1 + 3 * l[0]
        k1 -= l[0]
        answer += 2 * (l[1] - l[0])
        k1 -= l[1] - l[0]
        answer += k1 - 1
        print(answer)
