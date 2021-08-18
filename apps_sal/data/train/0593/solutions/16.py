t = int(input())
for i in range(t):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    a = list(map(int, input().split()))
    s = input()
    c = 0
    for j in alphabets:
        if j not in s:
            c += a[ord(j) - 97]
    print(c)
