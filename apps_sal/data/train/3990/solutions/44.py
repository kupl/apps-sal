def derive(coefficient, exponent): 
    product = coefficient*exponent
    exponent = exponent -1
    return'{}x^{}'.format(product,exponent)
