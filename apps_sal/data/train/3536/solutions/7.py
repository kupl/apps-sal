def cog_RPM(cogs, n):
    r=[cogs[n]/cogs[0],cogs[n]/cogs[-1]]
    if n%2==1:
        r[0]*=-1
    if (len(cogs)-n)%2==0:
        r[1]*=-1
    return r
