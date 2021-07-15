import math

def primeFactors(n):
    dic_prime = {}
    dic_prime[2] = 0
    while n%2 ==0:
        dic_prime[2] += 1
        n = n/2
    if dic_prime[2] == 0:
        dic_prime.pop(2)

    for i in range(3,int(n+1),2):
        dic_prime[i] = 0
        while n%i ==0:
            dic_prime[i] += 1
            n = n/i
        if n <= 1:
            break
        if dic_prime[i] == 0:
            dic_prime.pop(i)

    output_str = ""
    for k,v in dic_prime.items():
        if v == 1:
            output_str += "({})".format(str(k))
        else:
            output_str +="({}**{})".format(str(k),str(v))

    return output_str
