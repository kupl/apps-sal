from functools import cmp_to_key


def hull_method(pointlist):
    # handles the duplicate inputs
    pointlist = list(set(map(tuple, pointlist)))
    # find the bottom most and left most point
    first_idx = min(range(len(pointlist)), key=lambda x: (pointlist[x][1], pointlist[x][0]))
    pointlist[first_idx], pointlist[0] = pointlist[0], pointlist[first_idx]
    # sort from the first
    p = pointlist[0]

    def custom_compare(q, r):
        px, py = p
        qx, qy = q
        rx, ry = r
        compare = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)
        if compare < 0:
            return -1
        elif compare > 0:
            return 1
        else:
            return -1 if (rx - px)**2 + (ry - py)**2 >= (qx - px)**2 + (qy - py)**2 else 1

    def get_angle(p, q, r):
        px, py = p
        qx, qy = q
        rx, ry = r
        return (qy - py) * (rx - qx) - (qx - px) * (ry - qy)

    pointlist[1:] = sorted(pointlist[1:], key=cmp_to_key(custom_compare))
#     print("pointlist = ", pointlist)
    lst, i = [pointlist[0]], 2
    while i < len(pointlist):
        while i < len(pointlist) and get_angle(p, pointlist[i - 1], pointlist[i]) == 0:
            i += 1
        if i < len(pointlist):
            lst.append(pointlist[i - 1])
            i += 1
    lst.append(pointlist[i - 1])
#     print("sorted list = ", lst)
    if len(lst) < 3:
        return []
    stck = [lst[0], lst[1], lst[2]]
    for i in range(3, len(lst)):
        while get_angle(stck[-2], stck[-1], lst[i]) >= 0:
            stck.pop()
        stck.append(lst[i])
    return list(map(list, stck))
