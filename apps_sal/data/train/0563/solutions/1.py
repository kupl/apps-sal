# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = [int(k) for k in input().split()]
    q = int(input())
    for i in range(q):

        route = [int(k) for k in input().split()]
        sum = 0
        for j in range(route[0] - 1, route[1]):
            sum = sum + arr[j]

        print(sum)
