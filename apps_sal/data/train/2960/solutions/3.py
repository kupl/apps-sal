import fractions
def sum_differences_between_products_and_LCMs(pairs):
   return sum( [pair[0]*pair[1]*(1-(1.0/fractions.gcd(pair[0], pair[1]) if fractions.gcd(pair[0], pair[1])!=0 else 0)) for pair in pairs])
