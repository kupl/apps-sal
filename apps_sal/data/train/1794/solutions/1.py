# two numbers >= 2
def statement1(s):
    #task: determine if
    #sum determines that numbers cannot be determined from product without other info
    return not prime(s-2) and not s%2 == 0 
    #conclusion made:
    #--> sum is odd --> two numbers are even,odd
    #--> sum not prime + 2 --> two numbers are not 2,prime
def statement2(p):
    #task: determine if
    #numbers can be determined from product after knowing that statement 1 is true
    l = [i for i in factor_pairs(p) if (i[0]>=2 and i[1] >=2)]
    l_ = [i for i in l if statement1(sum(i))]
    return l != l_ and len(l_) == 1
    #conclusion made:
    #--> statement one is true about exactly one factor pair's sum --> statement one
    #(cont) is true about only one combination of numbers that make the sum
def statement3(s):
    #task: determine if
    #numbers can be determined from sum after knowing that statement 2 is true
    return len([(i,s-i) for i in range(2,s//2+1) if statement2(i*(s-i))])==1
def is_solution(a, b):
    #task: determine if
    #statement 1,two,and 3 are true about the two numbers
    return statement1(a+b) and statement2(a*b) and statement3(a+b)
def prime(x):
    #determines if a number is prime
    x = int(x)
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
def factor_pairs(x):
    res = set([])
    for i in range(1,x):
        if x%i == 0:
            res.add(tuple(sorted(([i,x/i]))))
    return sorted([[int(j) for j in i]for i in list(res)],key = lambda x: x[0])
