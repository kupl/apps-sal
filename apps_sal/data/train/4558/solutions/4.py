def penaltyShots(h,s):
    return 6-min(h,4)-abs(s[0]-s[1])
