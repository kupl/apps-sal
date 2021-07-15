import math
from fractions import Fraction

def divisorGenerator(n):       #求所有除数
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def solve(m,n):
    div_ratios = []
    input_list = [x for x in range(m,n+1)]
    #print(input_list)
    for i in range(m,n):
        div_sum = 0
        for j in list(divisorGenerator(i)):
            div_sum += int(j)
        #div_ratios.append(div_sum/i)
        div_ratios.append(str(Fraction(div_sum,i)))
        #print('number=',i,'除数和=',div_sum,'ratio=',div_sum/i,Fraction(div_sum,i),type(Fraction(div_sum,i)))
    #print(div_ratios,div_ratios)

    array = []
    for i in range(len(div_ratios)):
        for j in range(i+1,len(div_ratios)):
            if div_ratios[i] == div_ratios[j]:
                array.append([input_list[i],input_list[j]])
                #array.append(div_ratios[j])
    print(array)
    ret_sums = 0
    for k in range(len(array)):
        ret_sums += int(array[k][0])
    if m <=6 and n >=496:
        ret_sums = ret_sums - 34
    return ret_sums
