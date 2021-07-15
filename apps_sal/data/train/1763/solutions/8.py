def comb(n,k):
    c=1
    for i in range(n,n-k,-1):
        c*=i
    for i in range(1,k+1):
        c//=i
    return c

def insane_inc_or_dec(max_digits):
    increasing=comb(max_digits+9,9)-1
    decreasing=comb(max_digits+10,10)-max_digits-1
    return (increasing+decreasing-9*max_digits+1-1)%12345787
