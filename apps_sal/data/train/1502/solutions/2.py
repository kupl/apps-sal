for _ in range(int(input())):
    string = input().strip()
    n = int(input())
    lst = input().split()
    status = True
    for x in string:
        if x not in lst:
            status = False
            break
    if status:
        print(1)
    else:
        print(0)
