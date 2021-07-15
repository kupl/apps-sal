def primeFactors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if(i in factors.keys()):
                factors[i]+=1
            else:
                factors[i]=1
    if n > 1:
        factors[n]=1
    string=""
    for key in factors.keys():
        if factors[key]==1:
            string+="({})".format(key)
        else:
            string+="({}**{})".format(key,factors[key])
    return string
