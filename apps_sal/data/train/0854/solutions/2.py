for _ in range(int(input())):
    n = int(input())
    arr = sorted([int(k) for k in input().split()])
    res = True
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            res = False
            break
    if res:
        print('prekrasnyy')
    else:
        print('ne krasivo')
