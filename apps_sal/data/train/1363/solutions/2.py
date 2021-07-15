tts=[1,23]
mod=10**9+7
for x in range(2,2*10**6+1):
 tts.append(tts[x-1]*23%mod)

t=eval(input())
while t>0:
 n,d=list(map(int,input().split()))
 num=int(str(d)*n)
 num**=2
 res=0
 i=0
 for x in str(num):
  res+=((int(x)*tts[i]))
  i+=1
 print(res%mod)
 t-=1

