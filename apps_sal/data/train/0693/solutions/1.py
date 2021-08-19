# cook your dish here
for _ in range(int(input())):
    n = int(input())
    fact = 1
    if n == 0:
        pass
    else:
        for i in range(1, n + 1):
            fact *= i
    print(fact)
