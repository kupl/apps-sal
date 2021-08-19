t = eval(input())
for i in range(0, t):
    count = 0
    copies = eval(input())
    bats = [int(x) for x in input().split(' ')]
    standard = bats[0]
    for i in range(1, len(bats)):
        if bats[i] > standard:
            count = count + 1
    print(count)
