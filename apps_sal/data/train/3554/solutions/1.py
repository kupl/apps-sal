from collections import Counter
val = {1: [0, 100, 200, 1000, 2000, 3000, 4000],
       2: [0, 0  , 0  , 200 , 400 , 600 , 800 ],
       3: [0, 0  , 0  , 300 , 600 , 900 , 1200],
       4: [0, 0  , 0  , 400 , 800 , 1200, 1600],
       5: [0, 50 , 100, 500 , 1000, 1500, 2000],
       6: [0, 0  , 0  , 600 , 1200, 1800, 2400]}

def get_score(dice):
    C = Counter(dice)
    if len(C) == 6: return 1000
    if len(C) == 3 and all(map((2).__eq__, C.values())): return 750
    return sum(val[k][v] for k,v in C.items()) or "Zonk"
