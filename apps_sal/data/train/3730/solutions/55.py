def capitalize(s):
    final1 = ""
    final2 = ""
    
    for x in range(len(s)):  #1st string
        final1 += s[x].upper() if x%2==0 else s[x]
            
    for x in final1: #toggle 1st string to get the 2ns string
        final2 += x.lower() if x.isupper() else x.upper()
            
    return [final1,final2]
