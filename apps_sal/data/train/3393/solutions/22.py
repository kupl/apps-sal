A={}
for n in range(1,12000):
    A[n] = [j**2 for j in list(range(1,int(n/2)+1))+[n] if (n/j).is_integer()]
    
def list_squared(m, n):
    return [[i,sum(A[i])] for i in range(m,n+1) if (sum(A[i])**(1/2)).is_integer()]

