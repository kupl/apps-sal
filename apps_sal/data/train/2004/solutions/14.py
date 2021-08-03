from sys import stdin


def main():
    s = stdin.readline().strip()
    i = s.find('0')
    if i == -1:
        return s[:-1]
    else:
        return s[:i] + s[i + 1:]


print(main())
