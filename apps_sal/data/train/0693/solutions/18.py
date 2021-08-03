T = int(input())

for i in range(T):
    N = int(input())
    Number = 1
    for l in range(1, N + 1):
        Number *= l
    print(Number)
