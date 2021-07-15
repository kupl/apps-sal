power={1:2, 2:6, 3:11, 4:17, 5:25, 6:35, 7:46, 8:58, 9:72, 10:88,
       11:106, 12:126, 13:147, 14:170, 15:195, 16:221,
       17:250, 18:280, 19:311, 20:343}
def psion_power_points(level,score):
    if level==0 or score<=10:
        return 0
    return power.get(level,343)+level*((score-score%2)-10)//4
