def i_tri(s):
    t = 2.4 + 112.0 + 26.2
    v = t - s
    k = "Swim" if s < 2.4 else "Bike" if s >= 2.4 and s < 114.4 else 'Run'
    if s == 0: return 'Starting Line... Good Luck!'
    elif s >= t: return "You're done! Stop running!"
    elif t - s <= 10: return {'Run':'Nearly there!'}
    else: return {k: "{:.2f}".format(v) + ' to go!'}

