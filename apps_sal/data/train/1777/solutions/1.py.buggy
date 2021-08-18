rle = []
one_color_flag = 0
# @profile


def getline(w):
    nonlocal rle, one_color_flag
    rezl = []
    while w > 0:
        rle0 = rle[0]
        rle1 = rle[1]
        if rle1 > w:
            rle[1] -= w
            rezl.extend([rle0 for i in range(w)])
            one_color_flag += 1
            return rezl
        else:
            rezl.extend([rle0 for i in range(rle1)])
            one_color_flag = 0
            w -= rle1
            rle.pop(0)
            rle.pop(0)
    return rezl


# @profile
def edge_detection(rle_str):
    nonlocal rle, one_color_flag
    rle = [int(x) for x in rle_str.split(' ')]
    width = rle.pop(0)
    data_length = sum(rle[1::2])
    height = data_length // width
    width3 = width * 3
    rez = [width]
    width_bound = width - 1
    height_bound = height - 1
    l2 = getline(width)  # fill all window lines first line from image
    l1 = l2
    # print(l2)
    curr_dev = -99999
    y = 0
    while y < height:
        l0 = l1
        l1 = l2
        if y < height_bound:
            l2 = getline(width)
        # print(l2)
        x = 1

        # +++ first elem in line
        t = [l1[1], l0[0], l0[1], l2[0], l2[1]]
        # t.sort()
        #c = max(abs(t[0] - l1[0]),abs(t[-1] - l1[0]))
        c = max(abs(min(t) - l1[0]), abs(max(t) - l1[0]))
        if curr_dev == c:
            rez[-1] += 1
        else:
            rez.append(c)
            rez.append(1)
            curr_dev = c
        # --- first elem in line

        while x < width_bound:
            t = [l1[x - 1], l1[x + 1], l0[x - 1], l0[x], l0[x + 1], l2[x - 1], l2[x], l2[x + 1]]
            # t.sort()
            #c = max(abs(t[0] - l1[x]),abs(t[-1] - l1[x]))
            c = max(abs(min(t) - l1[x]), abs(max(t) - l1[x]))
            if curr_dev == c:
                rez[-1] += 1
            else:
                rez.append(c)
                rez.append(1)
                curr_dev = c
            x += 1
        # +++ end elem in line
        t = [l1[-2], l0[-2], l0[-1], l2[-2], l2[-1]]
        # t.sort()
        #c = max(abs(t[0] - l1[-1]),abs(t[-1] - l1[-1]))
        c = max(abs(min(t) - l1[-1]), abs(max(t) - l1[-1]))
        if curr_dev == c:
            rez[-1] += 1
        else:
            rez.append(c)
            rez.append(1)
            curr_dev = c
        # --- end elem in line
        y += 1

        # if rez[-1] > width3 and y < height_bound and l1[0] == rle[0] :
        if one_color_flag > 2:
            n_str = (rle[1] // width) - 1
            one_color_flag = 0
            if n_str > 0:
                ls = n_str * width
                #rez[-1] += ls
                if curr_dev == 0:
                    rez[-1] += ls
                else:
                    rez.append(0)
                    rez.append(ls)
                    curr_dev = 0
                rle[1] -= ls
                y += n_str

    return str(rez).replace(',', '').replace('[', '').replace(']', '')
