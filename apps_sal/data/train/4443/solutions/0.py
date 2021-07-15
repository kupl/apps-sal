"""
h = vt-0.5gt^2
let h = 0 [that is, when the ball has returned to the ground]
=> 0 = vt-0.5gt^2
=> 0.5gt^2 = vt
=> 0.5gt = v
=> t = 2v/g - the total time the ball is in the air.
=> t at max height  = v/g
"""

def max_ball(v0):
    return round(10*v0/9.81/3.6)
