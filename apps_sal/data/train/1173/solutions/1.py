# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    count = 0
    for i in range(0, n):
        sum = a[i]
        for j in range(i + 1, n):
            sum = sum ^ a[j]
            # print(sum)
            if(sum == 0):
                count = count + (j - i)

    print(count)
