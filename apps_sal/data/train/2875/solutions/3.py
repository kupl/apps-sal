import re

SEQ_PATTERN = re.compile(r'\.img')

def sort_photos(pics):
    sortedPics = sorted( list(map(int, SEQ_PATTERN.split(p))) + [p] for p in pics)
    lastY, lastN, _ = sortedPics[-1]
    return [p for _,_,p in sortedPics[-5:]] + ["{}.img{}".format(lastY, lastN+1)]
