get_military_time=lambda t:'%02d%s'%(int(t[:2])%12+12*(t[-2]>'A'),t[2:-2])
