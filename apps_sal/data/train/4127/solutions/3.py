import math
def divisorGenerator(n):       #求所有除数
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
        
def count_pairs_int(diff, n_max):
    div_num = []
    count = 0
    for i in range(1,n_max+1):
        div_num.append(len(list(divisorGenerator(i))))
    print(div_num,len(div_num))
    for j in range(diff,len(div_num)-1):
        #print(j,':','div_num[',j+1,']=',div_num[j+1],'div_num[',j,']=',div_num[j],'diff=',div_num[j+1]-div_num[j])
        if div_num[j] == div_num[j-diff]:
            count += 1
    return count
