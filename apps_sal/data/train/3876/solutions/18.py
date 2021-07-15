def find(n):
    sum3 = sum([3*i for i in range(1,n//3+1)])
    sum5 = sum([5*j for j in range(1,n//5 +1) if j%3 != 0])
    return sum3+sum5
    

