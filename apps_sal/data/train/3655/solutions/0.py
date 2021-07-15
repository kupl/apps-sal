def my_crib(n):
    roof = "\n".join("%s/%s\\%s"%(" "*(n-i)," "*i*2," "*(n-i)) for i in range(n))
    ceiling = "\n/%s\\\n"%("_"*(n*2))
    walls = ("|%s|\n"%(" "*(n*2)))*(n-1)
    floor = "|%s|"%("_"*(n*2))
    
    return roof + ceiling + walls + floor
