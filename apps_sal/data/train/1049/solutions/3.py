# cook your dish here
try:
    tc = int(input())
    for i in range(tc):
        n, k = list(map(int, input().split(" ")))
        arr = list(map(int, input().split()))
        set_arr = set(arr)
        max_sum = 0
        for i in range(n):
            if set(arr[i:i + k]) == set_arr:
                max_sum = max(max_sum, sum(arr[i:i + k]))
        print(max_sum)
except:
    pass
