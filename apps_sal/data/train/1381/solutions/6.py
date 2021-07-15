for _ in range(int(input())):
    n,k,d = [int(a) for a in input().split()]
    blocks = [int(a) for a in input().split()]
    lanes = list(map(int, input().split()))

    Flag = 0
    z = -10000000000000
    for i in range(n-1):
     if lanes[i] != lanes[i+1]:
      z = max(blocks[i]+1, z+d)
      if z >= blocks[i+1]:
       print(blocks[i+1])
       Flag = 1
       break
    if Flag == 0:
     print(k)
 

  
  

