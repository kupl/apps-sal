odd_dig_cubic=lambda a,b:[n**3for n in range(int(a//abs(a or 1)*abs(a)**3**-1)|1,int(b//abs(b or 1)*abs(b)**3**-1)|1+2,2)if a<=n**3<=b and set(str(n**3))<=set('-13579')]
