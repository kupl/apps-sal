def key(pic):
    parts = pic.split('.')
    return (parts[0], int(parts[1][3:]))


def sort_photos(pics):
    pics.sort(key=key)
    pics = pics[-5:]
    last_key = key(pics[-1])
    pics.append(last_key[0] + '.img' + str(last_key[1] + 1))
    return pics
