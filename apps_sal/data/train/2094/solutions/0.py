def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = input()
    one = arr.count('n')
    zero = arr.count('z')
    ans = [1] * one + [0] * zero
    print(*ans)
    return 0


main()
