def statement1(s):
    return not prime(s-2) and not s%2 == 0
def statement2(p):
    l = [i for i in factor_pairs(p) if (i[0]>=2 and i[1] >=2)]
    l_ = [i for i in l if statement1(sum(i))]
    return l != l_ and len(l_) == 1
def statement3(s):
    return len([(i,s-i) for i in range(2,s//2+1) if statement2(i*(s-i))])==1
def is_solution(a, b):
    return statement1(a+b) and statement2(a*b) and statement3(a+b)
def prime(x):
    for i in range(2,int(x)):
        if int(x) % i == 0:
            return False
    return True
def factor_pairs(x):
    res = set([])
    for i in range(1,x):
        if x%i == 0:
            res.add(tuple(sorted(([i,x/i]))))
    return sorted([[int(j) for j in i]for i in list(res)],key = lambda x: x[0])
