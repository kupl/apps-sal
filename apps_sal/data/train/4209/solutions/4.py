def largest_rect(histogram):
    dim = len(histogram)
    if dim == 0:
        return 0
    max_el = max(histogram)
    min_el = min(histogram)
    if max_el == min_el:
        return dim * max_el
    area = max_el if max_el > min_el * dim else min_el * dim

    arr_work = [histogram]
    while len(arr_work) > 0:
        h = arr_work.pop()
        dim = len(h)
        max_el = max(h)
        min_el = min(h)
        if max_el * dim < area:
            continue
        if max_el == min_el:
            if area < dim * max_el:
                area = dim * max_el
            continue
        area = min_el * dim if area < min_el * dim else area
        split_index = h.index(min_el)
        if split_index * max_el >= area:
            arr_work.append(list(reversed(h[:split_index])))
        if (dim - 1 - split_index) * max_el >= area:
            arr_work.append(list(reversed(h[(split_index + 1):])))

    return area
