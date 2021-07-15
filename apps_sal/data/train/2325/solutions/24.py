s=input()
t=input()
q=int(input())
acums=[[0,0] for _ in range(len(s)+1)]
for i in range(1,len(s)+1):
  if s[i-1]=='A':
    acums[i][0]=acums[i-1][0]+1
    acums[i][1]=acums[i-1][1]
  else:
    acums[i][0]=acums[i-1][0]
    acums[i][1]=acums[i-1][1]+1
acumt=[[0,0] for _ in range(len(t)+1)]
for i in range(1,len(t)+1):
  if t[i-1]=='A':
    acumt[i][0]=acumt[i-1][0]+1
    acumt[i][1]=acumt[i-1][1]
  else:
    acumt[i][0]=acumt[i-1][0]
    acumt[i][1]=acumt[i-1][1]+1
for _ in range(q):
  a,b,c,d=map(int,input().split())
  cnt1=(acums[b][0]-acums[a-1][0])*2+(acums[b][1]-acums[a-1][1])
  cnt2=(acumt[d][0]-acumt[c-1][0])*2+(acumt[d][1]-acumt[c-1][1])
  if (cnt1-cnt2)%3==0:
    print('YES')
  else:
    print('NO')
