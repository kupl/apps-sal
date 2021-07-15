for _ in range(int(input())):
 N = int(input())
 seq = list(map(int,input().split()))
 maxx = max(seq)
 count = 0
 seq = seq+seq
 max_cont = 0
 for i in range(2*N):
  if seq[i] != maxx:
   count +=1
  else:
   if count > max_cont:
    max_cont = count
   count = 0
 if count > max_cont:
  max_cont = count
 print(max(max_cont-N//2+1,0))
