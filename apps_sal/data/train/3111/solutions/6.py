import re
def number_format(n):
    # converts int to str, reverses it for next step
    n = str(n)[::-1]
    
    # split into groups of 3 digits
    g = re.split(r'(\d{3})', n)
    
    # remove empty string from list
    g = list(filter(None, g))
    
    # special case where "-" is only char in a group and messes up with ",".join()
    if g[-1] == "-":
        return g[-1] + ','.join(g[:-1])[::-1]
    return ','.join(g)[::-1]
