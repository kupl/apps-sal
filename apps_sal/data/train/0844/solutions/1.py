N, K = list(map(int, input().split()))
estado = [False]*N
numAbiertos=0
for _l in range(K):
 cmd = input().strip()
 if cmd=="CLOSEALL":
  estado=[False]*N
  numAbiertos=0
 else :
  num = int(cmd.split()[1])-1
  if estado[num] :
   estado[num]=False
   numAbiertos -= 1
  else :
   estado[num]=True
   numAbiertos += 1
 
 print(numAbiertos)

