def better_than_average(cp, yp):
     av= (yp + sum(cp))/ (len(cp)+1)
     if av > yp:
         return False
     return True

