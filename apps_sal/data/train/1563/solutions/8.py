N = int(input())
i = 0
while i < N:
    a = input()
    a = list(a)
    a.reverse()
    a = ''.join(a)
    a = a.split()
    a = int(a[0]) + int(a[1])
    a = list(str(a))
    a.reverse()
    a = ''.join(a)
    a = str(int(a))
    i = i + 1
    print(a)
