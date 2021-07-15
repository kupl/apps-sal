import re
from collections import Counter

def cards_and_pero(s):
    cardDeck = re.findall(r'([PKHT])(\d{2})', s)
    cnt      = Counter(suit for suit,_ in cardDeck)
    return [-1]*4 if len(set(cardDeck)) != len(cardDeck) else [ 13-cnt[suit] for suit in "PKHT"]
