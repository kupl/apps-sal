def sumin(n):
#     return sum(min(x+1,y+1) for y in range(n) for x in range(n))
    return sum((i+1)*(2*(n-i)-1) for i in range(n))
            
def sumax(n):
#     return sum(max(x+1,y+1) for y in range(n) for x in range(n))
    return sum((n-i)*(2*(n-i)-1) for i in range(n))
def sumsum(n):
    return sumin(n) + sumax(n)
