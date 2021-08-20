import sys


def main():
    s = sys.stdin.readline
    (n, m) = list(map(int, s().split()))
    nums = {}
    for i in range(1, n + 1):
        nums[i] = list(map(int, s().split()))
    cases = int(s())
    for case in range(cases):
        (px, py, qx, qy) = list(map(int, s().split()))
        ans = []
        for i in range(px, qx + 1):
            for j in range(py - 1, qy):
                ans.append(nums[i][j])
        print(sum(ans))


def __starting_point():
    main()


__starting_point()
