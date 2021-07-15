def animals(heads, legs):
    if 1000 >= heads < 0 or 1000 >= legs < 0 : return 'No solutions'
    if heads < 0 and legs < 0 : return 'No solutions'
    if heads == 0 and legs == 0: return (0, 0)
    if legs%2 != 0: return 'No solutions'
    cows = int(legs/2-heads)
    chickens = int(heads - cows)
    if cows >= 0 and chickens >= 0: return (chickens, cows)
    else: return "No solutions"
    
    
'''“A farm contains chickens and cows. There are x heads and y 
legs. How many chickens and cows are there?”

Where x <= 1000 and y <=1000


Return a tuple in Pythons

If either the heads & legs is negative, the result of your calculation is negative or 
the calculation is a float return "No solutions" (no valid cases).'''
