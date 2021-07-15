SCORE={"accounts": 1, "finance" : 2, "canteen" : 10, "regulation" : 3, "trading" : 6, 
       "change" : 6, "IS" : 8, "retail" : 5, "cleaning" : 4, "pissing about" : 25}
       
def boredom(staff):
  score = sum(map(lambda x: SCORE[x], staff.values()))
  return ("kill me now", "i can handle this", "party time!!")[(score>=100) + (score>80)]
