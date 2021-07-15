import math
n, h = [float(x) for x in input().split()]
base=1
ctgL= (base/2)/h

expectedArea = (1*h/2)/n
expectedArea=expectedArea/2

new_base = base/2
curr_height = h

def bin_search(new_base, min_height, max_height):
    try_height = (min_height+max_height)/2
    area = ((2*new_base - try_height*ctgL)/2)*try_height
    if(abs(area-expectedArea)<1e-9):
        return try_height
    else:
        if area>expectedArea:
            return bin_search(new_base, min_height,try_height)
        else:
            return bin_search(new_base, try_height, max_height)
def calculate_new_base(old_base, height):
    return old_base-height*ctgL
cuts = []
for i in range(int(n)-1):
    cut_height = bin_search(new_base, 0, curr_height)
    # print(cut_height)
    cuts.append(cut_height)
    new_base = calculate_new_base(new_base,cut_height)
    curr_height = curr_height - cut_height
    # print(new_base, curr_height)
cuts_sum=0
to_print = []
for cut in cuts:
    cuts_sum+=cut
    to_print.append((h-cuts_sum))
for x in reversed(to_print):
    print(x, end=" ")

