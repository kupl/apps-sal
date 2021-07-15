repeating_fractions=lambda n,d:str((n+0.0)/d).split('.')[0]+"."+"".join([["({})".format(i),i][len(list(j))==1]for i,j in __import__('itertools').groupby(str((n+0.0)/d).split(".")[1])])
