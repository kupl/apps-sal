def pass_the_bill(t, c, r):
    return 0 if c>=(t>>1)+1 else -1 if r>=(t>>1)+1 or r==t>>1 and t%2==0 else (t>>1)+1-c
