def animals(heads, legs):
    Chickens, Cows=  2*heads-legs/2, legs/2-heads
    if Chickens < 0 or Cows <0 or Chickens!= int (Chickens) or Cows!= int(Cows):
        return "No solutions"
    return (Chickens, Cows)

