#1は一意
#2は小さい番号の石の数が大きくなるように、大きい番号の石を除きたい

#個数が同順のものを、番号小以外が個数が時点になるまで除いてから、番号少を除く
n = int(input())
a = list(map(int, input().split( )))

cnt = {}#keyは個数、要素は最小番号

for i in range(n):
    if a[i] in cnt:
        cnt[a[i]][0] = min(cnt[a[i]][0],i)
        cnt[a[i]][1]+=1
    else:
        cnt[a[i]] = [i,1]

#個数、最小番号、番号の数    
mins = [[k,cnt[k][0],cnt[k][1]] for k in cnt]
mins.append([0,0,0])
#末端処理になっていない
mins.sort(reverse = True)
#print(mins)
ans = [0]*n

for i in range(len(mins)-1):
    k,cntk,l = mins[i][0],mins[i][1],mins[i][2]
    ans[cntk] += (k-mins[i+1][0])*l
    mins[i+1][2]+=l###=じゃおかしい
    if mins[i+1][1]>mins[i][1]:##追加
        mins[i+1][1] = mins[i][1]
#ans[mins[-1][1]]=n*mins[-1][0]

for ai in ans:
    print(ai)
    




