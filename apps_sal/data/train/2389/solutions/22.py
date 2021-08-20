import sys


def main():

    def diff(s, l):
        ret1 = [0 for k in range(len(s))]
        for k in range(len(s)):
            if k % 3 == 0 and s[k] != 'R':
                ret1[k] = 1
            if k % 3 == 1 and s[k] != 'G':
                ret1[k] = 1
            if k % 3 == 2 and s[k] != 'B':
                ret1[k] = 1
        ret2 = [0] * len(s)
        for k in range(len(s)):
            if k % 3 == 0 and s[k] != 'G':
                ret2[k] = 1
            if k % 3 == 1 and s[k] != 'B':
                ret2[k] = 1
            if k % 3 == 2 and s[k] != 'R':
                ret2[k] = 1
        ret3 = [0] * len(s)
        for k in range(len(s)):
            if k % 3 == 0 and s[k] != 'B':
                ret3[k] = 1
            if k % 3 == 1 and s[k] != 'R':
                ret3[k] = 1
            if k % 3 == 2 and s[k] != 'G':
                ret3[k] = 1
        s1 = [0] * (len(s) + 1)
        s2 = [0] * (len(s) + 1)
        s3 = [0] * (len(s) + 1)
        for k in range(1, n + 1):
            s1[k] = s1[k - 1] + ret1[k - 1]
            s2[k] = s2[k - 1] + ret2[k - 1]
            s3[k] = s3[k - 1] + ret3[k - 1]
        ans = 1000000
        for k in range(len(s) - l):
            ans = min(ans, s1[k + l] - s1[k], s2[k + l] - s2[k], s3[k + l] - s3[k])
        return ans
    input = sys.stdin.readline
    q = int(input())
    for query in range(q):
        (n, k) = list(map(int, input().split()))
        s = input()
        print(diff(s, k))


def __starting_point():
    main()


__starting_point()
