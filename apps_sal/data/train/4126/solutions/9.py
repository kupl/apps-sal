def what_time_is_it(angle):
    h=angle//30
    m=(angle%30)*2
    return '%02d:%02d'%(h,m) if h else '12:%02d'%m
