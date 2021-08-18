t = int(input())
for _ in range(t):
    s = list(''.join(input().split()))
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n = int("{}00".format(ord(s[0]) - 96))
    res = 0
    for i in s:
        res += (n + ord(i) - 97)
    print(res % 1000000007)
