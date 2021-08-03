from re import sub
def commas(num): return (lambda num: sub("(\d)(?=(\d{3})+(?!\d))", "\g<1>,", str(int(num) if num % 1 == 0 else num)))(round(num, 3))
