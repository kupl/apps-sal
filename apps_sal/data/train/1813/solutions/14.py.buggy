min_high_dict = {}

def minHigh( cw, mw, arr, ch):
    
    try:
        if min_high_dict[str(cw) +\" \" + str(len(arr))] != None:
            return min_high_dict[str(cw) +\" \" + str(len(arr))] 
    except KeyError:
        pass
    
    if len(arr) == 0:
        return ch
    
    elif cw == mw:
        re = max( arr[0][1], minHigh( cw-arr[0][0], mw, arr[1:], arr[0][1]))
    
    elif cw >= arr[0][0]:
        re1 = max( max(ch,arr[0][1]), minHigh( cw - arr[0][0], mw, arr[1:], max(ch,arr[0][1])))
        re2 = ch + minHigh( mw - arr[0][0], mw, arr[1:], arr[0][1])
        re = min( re1, re2)
    
    else:
        re = ch + minHigh( mw - arr[0][0], mw, arr[1:], arr[0][1])
    
    min_high_dict[str(cw) +\" \" + str(len(arr))] = re
    return re
    
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        min_high_dict.clear()
        return minHigh( shelf_width, shelf_width, books, 0)
