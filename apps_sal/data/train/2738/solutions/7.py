def i_tri(s):
    stages = [['Starting Line... Good Luck!'], [2.4, 'Swim'], [114.4, 'Bike'], [140.6, 'Run'], ['Nearly there!'], ["You're done! Stop running!"]]
    if not s:
        return stages[0][0]
    elif s >= 140.6:
        return stages[-1][0]
    else:
        curr_stage = [v for (k, v) in stages[1:4] if s <= k]
        return {curr_stage[0]: '{:.2f} to go!'.format(140.6 - s)} if s <= 130.6 else {curr_stage[0]: stages[4][0]}
