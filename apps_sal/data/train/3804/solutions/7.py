import math
box = []
for n in range(1001)[1:]:
    box.append(int(math.log10(sum(map(lambda x,y: x**y, list(range(n+1)), sorted(list(range(n+1)), reverse = True)))))+1)

def min_length_num(num, ord_max):
        floor = 0
        roof = ord_max
        while floor <=roof:
            mid = (roof+floor)//2
            if box[mid] > num:
                roof = mid - 1
            elif box[mid] < num:
                floor = mid + 1
            elif box[mid-1] == num:
                    floor -=1
                    roof -=1
            else:
                return [True, mid+1]
        else:
            return [False, -1]

