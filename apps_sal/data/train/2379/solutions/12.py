from collections import defaultdict
con = 10 ** 9 + 7
INF = float('inf')


def getlist():
    return list(map(int, input().split()))


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        s = list(map(int, list(input())))
        ans = [None] * N
        zeroend = []
        oneend = []
        zero_len = 0
        one_len = 0
        val = 0
        for i in range(N):
            if s[i] == 0:
                if one_len == 0:
                    val += 1
                    ans[i] = val
                    zeroend.append(val)
                    zero_len += 1
                else:
                    itr = oneend.pop()
                    ans[i] = itr
                    one_len -= 1
                    zeroend.append(itr)
                    zero_len += 1
            elif zero_len == 0:
                val += 1
                ans[i] = val
                oneend.append(val)
                one_len += 1
            else:
                itr = zeroend.pop()
                ans[i] = itr
                zero_len -= 1
                oneend.append(itr)
                one_len += 1
        print(val)
        print(*ans)


def __starting_point():
    main()


__starting_point()
