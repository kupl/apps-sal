def cal_n_bug(n_head, n_leg, n_wing):
    if n_head<0 or n_leg<0 or n_wing<0:
        return [-1,-1,-1]
    x=n_leg-6*n_head
    y=8*n_head-n_leg-n_wing
    z=n_leg+2*n_wing-8*n_head
    if x%2!=0 or z%2!=0 or x<0 or y<0 or z<0:
        return [-1,-1,-1]
    return [x//2,y,z//2]
