value = { "C" : "clubs",
          "D" : "diamonds",
          "H" : "hearts",
          "S" : "spades"
          }

def define_suit(card):
   return value.get(card[-1])
    

