n = int(input())
(a, b) = (1, 2)
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n + 1):
        c = (a + b) % 15746
        a = b
        b = c
    print(c % 15746)
