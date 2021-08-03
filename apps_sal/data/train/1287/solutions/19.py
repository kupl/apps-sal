t = int(input())
for j in range(t):
    s = input()
    n = len(s)
    e = 0
    for i in range(n):
        ch = s[i]
        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
            e += pow(2, (n - i - 1), 1000000007)
            e = e % 1000000007
    print(int(e))
