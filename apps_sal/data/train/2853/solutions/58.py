def solve(arr):
    # functional style
    def unique_recursive(src_arr, trg_arr):
        if len(src_arr) == 0:
            return trg_arr
        else:
            head, *tail = src_arr
            if head not in tail:
                trg_arr.append(head)
            return unique_recursive(tail, trg_arr)
    return unique_recursive(arr, [])
