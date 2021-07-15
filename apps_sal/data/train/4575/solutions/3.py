smallest_integer=lambda m:(lambda s:min({n+1for n in s if-1<=n}-s))(set(sum(m,[-1])))
