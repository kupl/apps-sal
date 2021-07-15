color_probability=lambda c, t, p=lambda x:x[0]in'bg':f"{([[2,1][p(c)],4][c[0]=='r']if p(t)else 1)/(7if p(t)else 3):.3f}"[:-1]
