def get_function(l):
    return 'Non-linear sequence' if any(l[i-1]+l[1]-l[0] != l[i] for i in (2,3,4)) else lambda x:(l[1]-l[0])*x+l[0] if l[1]-l[0] else l[0]
