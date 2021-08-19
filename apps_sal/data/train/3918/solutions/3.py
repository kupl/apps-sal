def baby_count(x):
    return min((x.lower().count(e) // (2 - (e != 'b')) for e in 'bay')) or "Where's the baby?!"
