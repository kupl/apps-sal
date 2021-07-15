def josephus_survivor(n,k):
    if (n == 1): 
          return 1 
    else: 
          r = list(range(1, n+1))
          sum = 0
          for i in r:
              sum = (sum+k) % i
          return sum + 1
        
        

