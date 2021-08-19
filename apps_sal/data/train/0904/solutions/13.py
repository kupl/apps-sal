import heapq
for i in range(int(input())):
    n, x = list(map(int, input().split()))
    list1 = list(map(int, input().split()))
    if(n == 2):
        if(max(list1) >= x):
            print("YES")
        else:
            print("NO")
        continue
    i = 1
    j = n - 2
    ans = 0
    flg = 0
    list2 = [max(list1[0], list1[-1])]
    heapq.heapify(list2)
    while(j >= i):
        max1, min1 = max(list1[i], list1[j]), min(list1[i], list1[j])
        if(i == j):
            heapq.heappush(list2, max1)
            break
        heapq.heappush(list2, max1)
        ele = heapq.heappop(list2)
        heapq.heappush(list2, max(min1, ele))
        i += 1
        j -= 1
    if(sum(list(list2)) >= x):
        print("YES")
    else:
        print("NO")  # cook your dish here
