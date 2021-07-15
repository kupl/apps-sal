def count(A, t, x):
    return sum(a%x==t%x for a in A) if x else sum(a==t for a in A)
