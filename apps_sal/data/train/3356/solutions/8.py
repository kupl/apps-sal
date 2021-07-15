three_amigos=lambda l:min(([a,b,c]for a,b,c in zip(l,l[1:],l[2:])if a%2==b%2==c%2),key=lambda t:max(t)-min(t),default=[])
