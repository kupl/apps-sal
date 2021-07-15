import math;

def Factor(n):
    a, d = [], 2;
    while d * d <= n:
        if n % d == 0:
            a.append(d);
            n //= d;
        else:
           d += 1;
    if n > 1:
       a.append(n);
    return a;

def proper_fractions(n):
    if(n == 1):
        return 0;
    used, k = [], 1;
    for i in Factor(n):
        if(i not in used):
            used.append(i);
            k *= math.pow(i, Factor(n).count(i)) - math.pow(i, Factor(n).count(i) - 1);
    return k;
