# cook your dish here
import sys


def get_factor(n: int):
    for i in range(2, int(n**0.5) + 1):
        if(n % i == 0):
            return i, n
    return n, n


N, M = sys.stdin.readline().strip().split(" ")[:2]

N, M = int(N), int(M)
if(N in (0, 1)):
    print(0)
# elif(N==1): print(2%M)
else:
    res = 2**N - 2
    f_, n_ = get_factor(N)
    if(f_ < N):
        res_ = [f_]
        res -= 2**(N // f_) - 2
        while(f_ < n_):
            f_, n_ = get_factor(n_ // f_)
            if(f_ not in res_):
                res_.append(f_)
                res -= 2**(N // f_) - 2
        if(n_ not in res_):
            res -= 2**(N // n_) - 2
#        if(N%(f_**2)==0):
#            res-=2**(N//f_)-2
#        else:
#            res-=2**(N//f_)-2+2**f_-2
    print(res % M)
