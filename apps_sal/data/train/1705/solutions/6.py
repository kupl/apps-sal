import math


def spidey_swings(ar):
    cur_pos = n = i = tz = 0
    ratio = thyp = None
    tome = []
    ln = len(ar)
    lim = int(math.sqrt(230 ** 2 - 200 ** 2))
    buildings = []
    for x in ar:
        tz += x[1]
        buildings.append(tz)
    end = buildings[-1]

    def find_index(r, g):
        for (q, z) in enumerate(r):
            if z > g:
                return q
        return -1
    while i < ln:
        (h, w) = ar[i]
        pt1 = buildings[i] - cur_pos
        pt0 = pt1 - w
        max_x = int(math.sqrt((h - 20) ** 2 - (h - 50) ** 2))
        if max_x >= pt0:
            max_x = min(pt1, max_x)
            ratio = [max_x, i] if ratio == None or max_x / math.hypot(max_x, h - 50) > ratio[0] / math.hypot(ratio[0], ar[ratio[1]][0] - 50) else ratio
        if buildings[i] - w >= cur_pos + lim:
            if end - lim * 2 < cur_pos:
                i += 1
                break
            npos = cur_pos + ratio[0] * 2
            tome.append(cur_pos + ratio[0])
            while n < ln and buildings[n] <= npos:
                n += 1
            cur_pos = npos
            i = n - 1
            ratio = None
        i += 1
    if cur_pos == end:
        return tome
    if cur_pos > end:
        cur_pos -= (cur_pos - tome.pop()) * 2
    tz = math.ceil((end - cur_pos) / 2)
    i = find_index(buildings, tz + cur_pos) + 1 or ln
    thyp = math.hypot(tz, ar[i - 1][0] - 50)
    if thyp > ar[i - 1][0] - 20:
        thyp = None
    for j in range(i, ln):
        (h, w) = ar[j]
        zz = math.hypot(h - 50, buildings[j - 1] - cur_pos)
        if zz <= h - 20:
            if thyp == None or thyp > zz:
                tz = buildings[j - 1] - cur_pos
                thyp = zz
                i = j
    if thyp == None:
        tome.append(cur_pos + ratio[0])
        cur_pos += ratio[0] * 2
        tz = math.ceil((end - cur_pos) / 2)
        i = find_index(buildings, tz + cur_pos) + 1 or ln
    final_val = [tz + cur_pos, math.hypot(tz, ar[i - 1][0] - 50)]
    for (q, z) in enumerate(ar[i:]):
        (h, w) = z
        hyp = math.hypot(buildings[i + q] - cur_pos - w, ar[i + q][0] - 50)
        if final_val[1] > hyp and hyp < ar[i + q][0] - 20:
            final_val = [buildings[i + q] - w, hyp]
    tome.append(final_val[0])
    return tome
