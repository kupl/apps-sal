f,count_perms=lambda n:n<1or n*f(n-1),lambda m:(lambda l:reduce(lambda x,y:x/f(l.count(y)),set(l),f(len(l))))(sum(m,[]))
