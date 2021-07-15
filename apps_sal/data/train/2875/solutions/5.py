def sort_photos(pics):
    pic2 = sorted([[int(i) for i in x.split('.img')] for x in pics])[-5:]
    return [str(i[0])+'.img'+str(i[1]) for i in pic2]+[str(pic2[-1][0])+'.img'+str(pic2[-1][1]+1)]
