value = { "C" : "clubs",
          "D" : "diamonds",
          "H" : "hearts",
          "S" : "spades"
          }

def define_suit(card):
    if card[-1] in value:
        return value.get(card[-1])

