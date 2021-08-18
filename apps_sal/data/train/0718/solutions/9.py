s = []


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


for _ in range(1, 101):
    s.append(fibonacci(_))
s[0] = 0


for _ in range(int(input())):
    n = int(input())
    p = 0
    for _ in range(1, n + 1):
        for __ in range(1, _ + 1):
            print(s[p], end=" ")
            p += 1
        print()
    print()
