def xMasTree(n):
   return [("#"*(x*2+1)).center(n*2-1, "_") for x in list(range(n))+[0]*2]
