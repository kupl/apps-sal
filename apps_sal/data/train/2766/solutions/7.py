def check_concatenated_sum(a,b):
    if not b:return False
    c=abs(a)
    d=[int(f"{(a<0)*'-'}{n*b}") for n in str(c)]
    return sum(d)==a
