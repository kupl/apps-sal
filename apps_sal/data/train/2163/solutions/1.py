from itertools import groupby

s=input()
n=len(s)
s=[s[i] for i in range(n)]
mod=10**9+7

data=groupby(s)
data=[(key,len(list(group))) for key,group in data]
Start=1
End=1
if data[0][0]=="0":
    Start+=data[0][1]
    data=data[1:]
if not data:
    print(Start-1)
    return

if data[-1][0]=="0":
    End+=data[-1][1]
    data.pop()

comp=[0]*len(data)
for i in range(len(data)):
    comp[i]=data[i][1]

n=len(comp)
if n==1:
    print(comp[0]*Start*End)
    return

odd=[comp[i] for i in range(n) if i%2==1]
N=len(odd)
N0 = 2**(N-1).bit_length()
data = [None]*(2*N0)
INF = (-1, 0)
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v

        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query(k):
    return _query(k)[1]

ID=[-1]*n
for i in range(N):
    start=0
    end=N
    while end-start>1:
        test=(end+start)//2
        if query(test)>=odd[i]:
            start=test
        else:
            end=test
    #print(i,start,odd[i])
    if start!=0:
        ID[2*i+1]=start
        update(start+1,i+1,(i,odd[i]))
    else:
        if query(0)>=odd[i]:
            ID[2*i+1]=start
            update(start+1,i+1,(i,odd[i]))
        else:
            ID[2*i+1]=-1
            update(0,i+1,(i,odd[i]))



dp=[0]*n
dp[0]=comp[0]
pre=[0]*n
for i in range(2,n,2):
    id=ID[i-1]
    if id==-1:
        res=comp[i-1]*dp[i-2]
        pre[i-1]=res
        #prel[i-1]=1
    else:
        j=2*id+1
        #res=(comp[i-1]*dp[i-2]+(comp[j]-comp[i-1])*premono[j])%mod
        res=(comp[i-1]*dp[i-2]+pre[j]-comp[i-1]*dp[j-1])%mod
        pre[i-1]=res
        #prel[i-1]=prel[j]+1
    dp[i]=(comp[i]*res+dp[i-2]+comp[i])%mod
#print(pre)
#print(dp)
print((dp[-1]*Start*End)%mod)

