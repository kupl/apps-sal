tc = int(input())
while tc != 0:
    size = int(input())
    data = []
    data = list(map(int, input().split()))
    i = 2
    count = 2
    max = 2
    while i < size:
        if data[i] == (data[i - 1] + data[i - 2]):
            count += 1
            if count > max:
                max = count
        else:
            count = 2
        i += 1
    print(max)
    tc -= 1
