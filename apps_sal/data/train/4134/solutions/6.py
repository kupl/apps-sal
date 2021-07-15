from math import ceil
def cooking_time(n_p,m,s,p):
    n_p,p=map(int,(n_p[:-1],p[:-1]))
    return "{} minutes {} seconds".format(*divmod(ceil((m*60+s)/p*n_p),60))
