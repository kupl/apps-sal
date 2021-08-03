from math import gcd
import sys
def input(): return sys.stdin.readline().strip()


def c(x): return 10**9 if(x == "?") else int(x)


def main():
    for _ in range(int(input())):
        s = list(input())[::-1]
        l = ['F', 'E', 'H', 'C']
        i = 0
        while(i < len(s)):
            if(i + 3 < len(s)):
                f = True
                for j in range(i, i + 4):
                    if(l[j - i] == s[j] or s[j] == '?'):
                        pass
                    else:
                        f = False
                        break
                if(f):
                    for j in range(i, i + 4):
                        s[j] = l[j - i]
                if(s[i] == "?"):
                    s[i] = 'A'
            else:
                if(s[i] == "?"):
                    s[i] = "A"
            i += 1
        print(*s[::-1], sep='')


main()
