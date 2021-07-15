def title_to_number(title):
    #your code here
    offset = ord('A') - 1
    radix = 26
    
    val = 0
    for i in title:
        val = radix * val + (ord(i) - offset)
        
    return val
