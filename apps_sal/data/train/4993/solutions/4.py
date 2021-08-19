import math


def temps(v0, slope, d_tot):

    GRAVITY_ACC = 9.81 * 3.6 * 60.0   # gravity acceleration
    DRAG = 60.0 * 0.3 / 3.6    # force applied by air on the cyclist
    DELTA_T = 1.0 / 60.0      # in minutes
    G_THRUST = 60 * 3.6 * 3.6   # pedaling thrust
    MASS = 80.0  # biker's mass
    WATTS0 = 225.0            # initial biker's power
    D_WATTS = 0.5

    t = 0

    grav = -GRAVITY_ACC * math.sin(math.atan(slope / 100))
    print(grav)

    v = v0
    watts = WATTS0
    s = 0
    a = 0
    while s <= d_tot:
        t += DELTA_T
        watts -= D_WATTS * DELTA_T

        drag = DRAG * abs(v) * abs(v) / MASS
        trst = (G_THRUST * watts) / (v * MASS)
        a = grav - drag + trst
       # print("G= ",grav,"Drag = ",drag," Trst= ",trst, "## A =", a)

        # print(a)
        if abs(a) <= 10**(-5):
            a = 0

        v = v + a * DELTA_T
        if v - 3.0 <= 0.01:
            return -1

        s = s + v * DELTA_T / 60
        # print(v)
        #print("s= ",s,"v= ",v,"a= ",a)
    print(t, s)

    return round(t)
