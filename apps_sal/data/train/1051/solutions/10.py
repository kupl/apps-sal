n = int(input())
for i in range(n):
    a = int(input())
    b = ''
    for j in range(0, a + 1):
        b = ''
        b = b + '*' * j + str(j)
        print(b)
