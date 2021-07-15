def find_missing_number(s):
    if not s: 
        return 0
    elif not all(x.isdigit() for x in s.split()):
        return 1
        
    s = sorted([int(i) for i in s.split()])
    if s[0] != 1:
        return 1
    
    a = [i for i in range(1,max(s)+1) if i not in s]
    return a[0] if len(a) > 0 else 0
