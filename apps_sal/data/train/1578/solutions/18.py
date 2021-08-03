n = int(input())

c = 0
sum = 0
while n:
    n -= 1
    a = [i for i in input()]
    sum = 0
    for i in a:
        try:
            sum += int(i)
        except:
            continue
    print(sum)
