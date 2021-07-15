N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
 
def sum_count(A,B,x):
    # A,B is sorted. 
    # return count(a+b < x)
    p = len(B)-1
    result = 0
    for a in A:
        while p != -1 and a + B[p] >= x:
            p -= 1
        result += p+1
    return result
 
		
def f(t,A,B):
    power = (1<<t)
    AA = [x&(2*power-1) for x in A]
    BB = [x&(2*power-1) for x in B]
    AA.sort()
    BB.sort()
    
    x1,x2,x3 = (sum_count(AA,BB,v) for v in [power, 2*power, 3*power])
    zero_cnt = x1 + (x3-x2)
    return (N-zero_cnt)%2
  
ans = 0
for t in range(30):
	x = f(t,A,B)
	if x == 1:
		ans += 1<<t
 
print(ans)
