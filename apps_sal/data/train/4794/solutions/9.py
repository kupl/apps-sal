def comfortable_numbers(l, r):
  sd = lambda x:sum(int(d) for d in str(x))
  return sum(sd(b+1)>=b-a+1 for a in range(l,r) for b in range(a,min(a+sd(a),r)))
