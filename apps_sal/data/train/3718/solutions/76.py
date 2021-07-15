def divisors(n):
    a = list(range(n));
    a.pop(0);
    c = [];
    for i in a:
        if n%i == 0:
            c.append(i);
    return(len(c) + 1);
