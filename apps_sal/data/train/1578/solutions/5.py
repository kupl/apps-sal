T = eval(input())
counter = 1


def ri():
    return list(map(int, input().strip().split()))


def rs():
    return input().strip().split()


def solve():
    S = rs()[0]
    ans = 0
    for i in S:
        if i.isdigit():
            ans += int(i)
    return ans


while T > 0:
    T -= 1
    print(str(solve()))
    counter += 1
