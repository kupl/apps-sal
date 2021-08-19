""" Considering that we search first 7000 Chandos numbers, generate the full
    list and then returned the good one on each call.
    
    Process: Chandos number are made of 5^n terms with DIFFERENT n, so integers
             usable as power can be represented in a binary way:
             
                 0    =>    no Chandos
                 1    =>    first Chandos: 5^1
                 10   =>    secund:        5^2
                 11   =>    ...            5^2 + 5^1
                 ...
             
             This way, the ARCHIVE is made by iterating binary numbers up to 7000
             in base 10.
             For the simplicity of the implementation, the binary representation is 
             reversed (-> big endian notation : this avoid the need of filling the 
             binary string representation with leading 0).
"""
ARCHIVE = [sum((5 ** (i + 1) for (i, s) in enumerate(reversed(bin(n)[2:])) if s == '1')) for n in range(1, 7001)]


def nth_chandos_number(n):
    return ARCHIVE[n - 1]
