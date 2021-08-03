# cook your dish here
for i in range(int(input())):
    N, K, V = map(int, input().split())
    list1 = []
    list1 = [int(x) for x in input().split()]
    total = (N + K) * V - sum(list1)
    avg = total / K
    average = total // K
    if(avg == average and avg >= 1):
        print(average)
    else:
        print("-1")
