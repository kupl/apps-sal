def is_hollow(A):
    while A and A[0]*A[-1]!=0:A=A[1:-1]
    return 2<A.count(0)and set(A)=={0}
