a = int(input())
for i in range(a):
    b = str(input()).split(' ')
    c = list(map(int, str(input()).split(' ')))
    Ans = int(b[1])
    c.sort(reverse=True)
    Ans += c[int(b[1]):int(b[0])].count(c[int(b[1]) - 1])
    print(Ans)
