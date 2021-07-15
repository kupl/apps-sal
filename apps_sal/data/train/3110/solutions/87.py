def two_decimal_places(n):
   return round(n+0.001,2) if str(n)[-1] == '5' else round(n,2)
