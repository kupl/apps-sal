a,b = map(int, input().split())


sum = 0
mod = 1000000007

def c(i):
    mi = i * b + i
    ma = i * b * a + i

    return ((mi+ma) * a)//2 

sum = (((c(1) + c(b-1))*(b-1))//2)%mod

print(sum)
