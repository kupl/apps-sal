T = int(input())
for i in range(T):
    N = input()
    s = list(N)
    t = s[::-1]
    if t == s:
        print(1)
    else:
        print(2)
