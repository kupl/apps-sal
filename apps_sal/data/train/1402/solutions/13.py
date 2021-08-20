def loji_hogya(a, b):
    count = 0
    while b > 0:
        u = a ^ b
        v = a & b
        a = u
        b = v * 2
        count = count + 1
    return count


n = int(input())
while n != 0:
    a = input()
    b = input()
    a = int(a, 2)
    b = int(b, 2)
    print(loji_hogya(a, b))
    n = n - 1
