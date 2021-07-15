import re

def derivative(eq):
    res = []
    
    # change bare "x"s to "1x" for easier processing
    eq = re.sub(r'\bx', '1x', eq)
    
    # extract constants, variables and exponents
    for const, var, exp in re.findall(r'([+-]?\d+)(x?)\^?(\d*)', eq):
        
        # if constant only, derivative = 0
        if not var:
            continue
        
        # if no exponent found (= 1), derivative = const
        if not exp:
            res.append(const)
            continue
        
        # if exponent > 1, calculate derivative
        const, exp = int(const), int(exp)
        const *= exp
        if exp == 2:
            res.append('%+dx' % const)
        else:
            res.append('%+dx^%d' % (const, exp - 1))
        
    # construct the final result and return it
    res = ''.join(res).strip('+')   
    return res if res else '0'

