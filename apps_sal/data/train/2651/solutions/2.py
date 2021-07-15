prod2sum=lambda a,b,c,d:sorted([list(i) for i in {tuple(sorted(map(abs,[(a*d)+(b*c),(a*c)-(b*d)]))),tuple(sorted(map(abs,[(a*c)+(b*d),abs((a*d)-(b*c))])))}])
