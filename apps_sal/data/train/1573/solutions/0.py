# cook your dish here
a = int(input())
for i in range(a):
    n = int(input())
    if n % 2 == 0:
        print('NO')
    else:
        print('YES')
        for i1 in range(n):
            li = [0] * n
            b = str()
            for i2 in range((n - 1) // 2):
                li[(i1 + i2 + 1) % n] += 1
            for i3 in range(len(li)):
                b += str(li[i3])
            print(b)
