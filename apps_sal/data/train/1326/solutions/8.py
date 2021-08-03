for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    su = arr[0]
    count = 0
    for j in range(1, n):
        if(su == 0):
            break
        else:
            su = (su - 1) + arr[j]
            count += 1
    print(su + count)
    arr.clear()
