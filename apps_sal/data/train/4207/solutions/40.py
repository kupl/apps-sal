def sum_cubes(n):
    sum=0
    for num in range(0,n+1):
      num=num*num*num
      sum=sum+num
    return sum   
