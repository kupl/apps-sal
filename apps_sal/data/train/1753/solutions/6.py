def least_bribes(bribes):
    d = dict()
    result = dp_worst_case(d, 0, len(bribes) - 1, bribes)
    return result
    
def dp_worst_case(d, start, end, l):
    # DP to re-use results
    if start in d:
        if end in d[start]:
            return d[start][end]
            
    diff = end - start
    
    if diff == 0:
        return l[start]
    elif diff == 1:
        return l[start] + l[end]
    elif diff == 2:
        # For 3 doors, the worst case is having to open 2 (doors [2,1] or [2,3]). You never have to open 3.
        return max([l[start+1] + l[start], l[start+1] + l[end]])
    else:
        anchor_wc_list = list()
        # Iterate over every anchor door ...
        for i in range(diff + 1):
            # ... except the first and last one of a (sub)list (they don't have to be visited "first")
            if i == 0 or i == diff:
                continue
            else:
                # work on the nonlocal list scale instead of the local loop list scale
                anchor = start + i
                # get left and right "branch" worst cases for the resp. anchor
                wcleft = l[anchor] + dp_worst_case(d, start, anchor - 1, l)
                wcright = l[anchor] + dp_worst_case(d, anchor + 1, end, l)
                # find the "worse" worst case of the left and right branch
                anchor_wc_list.append(max([wcleft, wcright]))
        # the result is the "best" worst case for all anchors
        result = min(anchor_wc_list)
        
        # save results for DP
        if start in d:
            d[start][end] = result
        else:
            d[start] = dict()
            d[start][end] = result
        return result
