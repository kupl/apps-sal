from math import factorial
t = int(input())
for _ in range(t):
    line = input()
    char = []
    for i in line:
        char.append(i)
    char.sort()
    same = []
    current = char[0]
    k = 0
    for i in char:
        if i == current:
            k += 1
        else:
            current = i
            if k > 1:
                same.append(k)
            k = 1
    same.append(k)
    ans = factorial(len(char))
    for i in same:
        ans //= factorial(i)
    print(ans % 1000000007)
