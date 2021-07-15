for _ in range(int(input())):
    n = input().strip()
    count = 0
    for i in n:
        if i != '4' and i != '7':
            count+=1
    print(count)
