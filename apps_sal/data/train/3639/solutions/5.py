stops = {'Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway'}

def alan(lst):
    return "No, seriously, run. You will miss it." if (stops - set(lst)) else "Smell my cheese you mother!"
