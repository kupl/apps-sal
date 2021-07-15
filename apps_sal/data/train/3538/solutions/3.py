from math import*;scroller=lambda t,a,p:"\n".join(" "*round(a+a*sin(i/p*tau))+c for i,c in enumerate(t))
