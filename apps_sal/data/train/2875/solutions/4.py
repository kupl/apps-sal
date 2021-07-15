def sort_photos(pics):
    s=[[int(i.split('.img')[0]), int(i.split('.img')[1])] for i in pics]
    s.sort()
    s.append([s[-1][0], s[-1][1]+1])
    return [(str(i[0]) + ".img" + str(i[1])) for i in s][-6:]
