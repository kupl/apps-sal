def my_crib(n):
    req, space = 3 + (2 * (n - 1)), 3 + (2 * ((n + (n * 2)) - 1))
    door = (space - 2) - (n * 4)
    roof =[[('_'*req).center(space,' ')] +
           [('/'+'_'*(req+(2*i))+'\\').center(space,' ') for i in range(n*2)] + 
           ['|'+' '*(space-2)+'|' for i in range(n-1)] +
           ['|'+(' '*n*2)+('_'*door)+(' '*n*2)+'|'] +
           ['|'+' '*(n*2-1)+'|'+' '*door+'|'+' '*(n*2-1)+'|' for i in range(n-1)] + 
           ['|'+'_'*(n*2-1)+'|'+'_'*door+'|'+'_'*(n*2-1)+'|']]
    return "\n".join(roof[0])
