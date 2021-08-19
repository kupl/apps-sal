t = int(input())
while t > 0:
    t -= 1
    sum = 0
    a = input()
    b = list(a)
    for i in b:
        if i.isdigit():
            sum += int(i)
    print(sum)
