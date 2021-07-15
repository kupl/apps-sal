def split_odd_and_even(n):
    
    import re
  
    return [int(i) for i in re.findall(r"[2468]+|[13579]+", str(n))]
