def largest_rect(histogram):
    (stack, max_area) = ([], 0)
    for (i, h) in enumerate(histogram + [0]):
        while stack and h <= histogram[stack[-1]]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
