def meeting_time(Ta, Tb, r):
    return str(abs(Tb))+'.00' if Ta == 0 else str(abs(Ta))+'.00' if Tb == 0 else str(round(abs(Ta*Tb/(Ta - Tb)), 4))+'0' if Ta != 0 and Tb != 0 and len(str(round(abs(Ta*Tb/(Ta - Tb)), 4))[str(round(abs(Ta*Tb/(Ta - Tb)), 4)).index('.')+1:]) == 1 else str(round(abs(Ta*Tb/(Ta - Tb)), 2))

