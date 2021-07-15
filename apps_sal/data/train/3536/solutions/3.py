def cog_RPM(cogs, n):
    a,b=1,1
    if n%2==1:
        a = -1
    if len(cogs)%2==n%2:
            b = -1
    return [a*cogs[n]/cogs[0],b*cogs[n]/cogs[-1]]
