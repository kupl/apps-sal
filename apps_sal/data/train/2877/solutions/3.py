def count(a, t, x):
    return sum((t-i)%x==0 for i in a) if x else sum(i==t for i in a)
