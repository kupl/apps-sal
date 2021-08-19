def f(s):
    s = list(s)
    cost = count = 0
    for i in s:
        if count == 6:
            count = 0
            continue
        else:
            count += 1
            if i == 'M':
                cost += 3
            else:
                cost += 4
    return cost


t = int(input())
for i in range(t):
    s = input()
    print(f(s))
