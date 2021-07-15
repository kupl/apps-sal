try:
    n=int(input())
    nums=[]
    t=int(input())
    nums.append(t)
    print(1)
    for _ in range(n-1):
        t=int(input())
        nums.append(t)
        z=sorted(nums,reverse=True)
        rank=z.index(t)
        print(rank+1)
  
except:
  pass
