from itertools import groupby


def largest_rect(histogram):
    histogram.append(0)
    stack = [-1]
    result = 0
    for i in range(len(histogram)):
        while histogram[i] < histogram[stack[-1]]:
            h = histogram[stack.pop()]
            w = i - stack[-1] - 1
            result = max(result, h * w)
        stack.append(i)
    histogram.pop()
    return result
