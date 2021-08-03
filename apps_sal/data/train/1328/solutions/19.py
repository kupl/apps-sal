for i in range(int(input())):
    count = 0
    num = input().strip()
    for i in num:
        if i != '4' and i != '7':
            count += 1
    print(count)
