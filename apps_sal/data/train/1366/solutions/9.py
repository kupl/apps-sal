    # cook your dish here
try:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        total = sum(arr)
        if total == 0:
            print(1)
        else:
            start = 0
            while arr[start]==0:
                start += 1
            x = 0
            count = 0
            for i in range(start,len(arr)):
                if x == total:
                    break
                else:
                    x += arr[i]
                    count += 1
            print(count)
except:
    pass
