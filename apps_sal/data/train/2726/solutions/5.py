import math

def square_it(digits):
    strdigits = str(digits)
    sq = math.sqrt(len(strdigits))
    if(round(sq,0) == sq):
      arr = []
      sqint = int(sq)
      for a in range(0,sqint):
        line = ""
        for b in range(0,sqint):
          line += strdigits[a*sqint+b]
        arr.append(line)
      return "\n".join(arr)
    else:
      return "Not a perfect square!"

