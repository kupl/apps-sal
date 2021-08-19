import sys
input = sys.stdin.readline


def main():
    (n, l) = map(int, input().split())
    words = []
    words = [input().rstrip() for _ in range(n)]
    s_words = sorted(words, key=lambda x: x[0:])
    ans = ''
    for s_word in s_words:
        ans += s_word
    print(ans)


def __starting_point():
    main()


__starting_point()
