def sort_photos(pics):
    tmp = sorted((pic[:8], int(pic[8:])) for pic in pics)
    return [x+str(y) for x,y in tmp[-5:]] + [tmp[-1][0] + str(tmp[-1][1] + 1)]
