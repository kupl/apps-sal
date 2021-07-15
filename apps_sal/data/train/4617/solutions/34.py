def powers_of_two(n):
    v=[];
    i=0;
    while i <= n:
        v.append(2**i);
        i+=1;
    return v;
