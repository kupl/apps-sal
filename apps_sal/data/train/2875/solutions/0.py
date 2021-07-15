def sort_photos(lst):
    lst = [[int(d) for d in f.split(".img")] for f in lst]
    s, l = sorted(lst), min(len(lst), 5)
    return [f"{y}.img{n+(i==l)}" for i, (y, n) in enumerate(s[-5:]+s[-1:])]

