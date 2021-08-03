# cook your dish here
t = int(input())
while(t):
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    count = 1
    i = 0
    cum_sum = arr[0]
    while(cum_sum < n - 1 - i):
        temp = cum_sum
        # print("temp=",temp)
        for x in range(i + 1, i + 1 + temp):
            cum_sum += arr[x]
        i += temp
        count += 1
        # print("left=",(n-i-1))
        # print("cum_sum=",cum_sum)
        # print("count=",count)
    print(count)
