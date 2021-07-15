def pattern(n):
    return '1\n'+'\n'.join(['1'+'*'*i+str(i+1) for i in range(1,n)] )

