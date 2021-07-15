def strong_num(number):   # performance version
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]   # factorial from 0-9
    digits = sorted([int(i) for i in str(number)])
    digits.reverse()
    
    s = 0
    for i in digits:
        s +=fac[i]
        if s > number: return "Not Strong !!"
        
    return "STRONG!!!!" if number == s else "Not Strong !!"
