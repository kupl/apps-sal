# cook your dish here
# from queue import PriorityQueue
import bisect
for _ in range(int(input())):
    n,l = map(int, input().split())
    a_l = list(map(int, input().split()))
    
    dic = {}
    dif = 0
    for i,v in enumerate(a_l, start=1):
        if v not in dic:
            dic[v] = [i, i]
        else:
            dic[v][0] = min(dic[v][0], i)
            dic[v][1] = max(dic[v][1], i)
            dif = max(dif, dic[v][1]-dic[v][0])
            
    ans = dif
    if l <= len(set(a_l)):
        i_l = [[v,i] for i,v in enumerate(a_l, start=1)]
        i_l.sort(reverse=True)
        
        dp = [[-1 for _ in range(l)] for _ in range(n)]
        pq_l = [[] for _ in range(l)]
        for i in range(1,n):
            il = 1
            dif_l = []
            for j in range(i):
                dif = abs(i_l[i][1]-i_l[j][1])
                dif_l.append(dif)
                dp[i][il] = max(dp[i][il], dif)
                
            for il in range(2,min(l,i+1)):
                for prev_max, ind in reversed(pq_l[il-1]):
                    if ind == i:
                        continue
                    if prev_max < dp[i][il]:
                        break
                    else:
                        dp[i][il] = max(dp[i][il], min(dif_l[ind], prev_max))
                tmp = [v[0] for v in pq_l[il]]
                ind = bisect.bisect_right(tmp, dp[i][il])
                pq_l[il].insert(ind, [dp[i][il], i])
                
            il = 1
            tmp = [v[0] for v in pq_l[il]]
            ind = bisect.bisect_right(tmp, dp[i][il])
            pq_l[il].insert(ind, [dp[i][il], i])
            
            # print(i, pq_l, dif_l)
                        
                
                # dp[i][1] = max(dp[i][1], dif)
                # for il in range(2,l):
                #     if dp[j][il-1] == -1:
                #         break
                #     dp[i][il] = max(dp[i][il], min(dif, dp[j][il-1]))
            ans = max(ans, dp[i][-1])
    #     print(dp)
    # print(dic)
    print(ans)
