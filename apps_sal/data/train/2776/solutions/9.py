from re import sub
commas = lambda num: (lambda num: sub("(\d)(?=(\d{3})+(?!\d))", "\g<1>,", str(int(num) if num%1==0 else num)))(round(num,3))
