for case in range(int(input())):
    jewels = set([])
    for char in input().rstrip('\n'):
        jewels.add(char)
    count = 0
    for char in input().rstrip('\n'):
        if char in jewels:
            count += 1
    print(count)
