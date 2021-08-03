n = int(input())
c = 0
for i in range(n):
    a = input()
    for i in a:
        if i.isdigit():
            c += int(i)
    print(c)
    c = 0
