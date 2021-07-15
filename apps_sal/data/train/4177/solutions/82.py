def men_from_boys(arr):
    
    m = [i for i in arr if i % 2 == 0]
    b = [i for i in arr if i % 2 != 0]
    
    s1 = set(m)
    s2 = set(b)
    
    return sorted(s1) + sorted(s2, reverse = True)
