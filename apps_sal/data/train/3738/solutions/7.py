class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize #makes things alot faster
def fib_spec(n): #that is the gain per station, so really we have to take the sum of all n's
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        k_1, s_1 = fib_spec(n-1)
        k_2, s_2 = fib_spec(n-2)
        return (k_1+k_2, s_1+s_2)


def calc(k,n,m,x):
    if x in (1,2):
        return k
    elif x == 3:
        return 2*k
    s_ = 0
    k_ = 1
    for i in range(n-3):
        tmp_k, tmp_s = fib_spec(i)
        s_ += tmp_s
        k_ += tmp_k
        if i == x-3:
            s_x, k_x = s_, k_
    s = (m-k*k_)//s_
    return k_x*k+s_x*s
