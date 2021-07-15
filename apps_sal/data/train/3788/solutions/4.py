from decimal import Decimal
p_num=lambda n: (lambda deltasq: ((1+deltasq)/6)%1==0)(Decimal(1+24*n).sqrt())
g_p_num=lambda n: (lambda deltasq: ((1+deltasq)/6)%1==0 or ((1-deltasq)/6)%1==0)(Decimal(1+24*n).sqrt())
s_p_num=lambda n: p_num(n) and Decimal(n).sqrt()%1==0
