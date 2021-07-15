def plane_seat(a):
    section = ['Front','Middle','Back',None]
    cluster = {'ABC':'Left','DEF':'Middle','GHK':'Right'}
    my_section = section[((int(a[:-1])-1)//20)]
    my_cluster = [v for k,v in cluster.items() if a[-1].upper() in k]
    return "No Seat!!" if not (my_section and my_cluster) else "{}-{}".format(my_section,my_cluster[0])
