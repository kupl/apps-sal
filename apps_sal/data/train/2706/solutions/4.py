pass_the_bill = lambda t, c, r: -1 if r / t >= 0.5 else max(0,int(t/2)+1-c)
