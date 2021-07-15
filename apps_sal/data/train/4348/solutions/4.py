def calc_fuel(n):
    dict={"lava": 0, "blaze rod": 0, "coal": 0, "wood": 0, "stick": 0 }
    time=n*11
    if time>=800:
        dict["lava"]=time//800
        time-=800*(time//800)
    if time>=120:
        dict["blaze rod"]=time//120
        time-=120*(time//120)
    if time>=80:
        dict["coal"]=time//80
        time-=80*(time//80)
    if time>=15:
        dict["wood"]=time//15
        time-=15*(time//15)
    dict["stick"]=time
    return dict
