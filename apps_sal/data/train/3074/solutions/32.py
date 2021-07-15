def growing_plant(upSpeed, downSpeed, desiredHeight):
    if upSpeed>=desiredHeight:
        return 1
    else:
        desiredHeight_after_first_day=desiredHeight-upSpeed
        increment_each_day=upSpeed-downSpeed
        if desiredHeight_after_first_day%(increment_each_day)==0:
            return desiredHeight_after_first_day//(increment_each_day)+1
        else:
            return desiredHeight_after_first_day//(increment_each_day)+2
    #your code here

