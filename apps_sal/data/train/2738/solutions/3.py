def i_tri(d):
    r, k = 140.6 - d, "Run" if 114.4 < d else "Bike" if 2.4 < d else "Swim"
    v = f"{r:.2f} to go!" if r > 10 else "Nearly there!"
    return {k: v} if d*r > 0 else "You're done! Stop running!" if d > 0 else "Starting Line... Good Luck!"

