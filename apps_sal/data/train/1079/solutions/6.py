n = int(input())
for i in range(n):
    s = 0
    a = input()
    for j in range(len(a)):
        if a[j] == '4':
            s += 1
    print(s)
