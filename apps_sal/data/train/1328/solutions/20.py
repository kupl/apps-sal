# cook your dish here
for _ in range(int(input())):
    N = input().strip()
    c = 0
    for i in N:
        if i != '4' and i != '7':
            c += 1

    print(c)
