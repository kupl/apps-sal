calculate_years = lambda p,i,t,d,n=0: calculate_years(p+(p*i*(1-t)),i,t,d,n+1) if p<d else n
