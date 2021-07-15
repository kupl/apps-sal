import heapq
t = int(input())

for loop in range(t):

    n = int(input())

    q = []
    q.append([-1*n,0,n-1])

    ans = [0] * n
    cnt = 1

    while len(q) > 0:

        tmppop = heapq.heappop(q)
        length,l,r = tmppop
        mid = (l+r)//2

        ans[mid] = cnt
        cnt += 1

        if mid-1 >= l:
            heapq.heappush(q,[-1 * ((mid-1)-l+1) , l , mid-1])
        if mid +1 <= r:
            heapq.heappush(q,[-1 * (r-(mid+1)+1) , mid+1 , r])

    print(*ans)

