a, b = map(int, input().split())
for i in range(b):
    r = a % 10
    n = a // 10
    if(r == 0):
        a = n
    else:
        a = a - 1
print(a)
