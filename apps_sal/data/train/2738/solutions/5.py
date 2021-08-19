def i_tri(s):
    # your code here
    d = {2.4: 'Swim', 114.4: 'Bike', 140.6: 'Run'}
    if s == 0:
        return 'Starting Line... Good Luck!'
    for k in sorted(d):
        if s < k:
            return {d[k]: "{:.02f} to go!". format(140.6 - s)}
    return "You're done! Stop running!"
