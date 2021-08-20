def expression_matter(a, b, c):
    tmp = [a, b, c]
    return max(tmp[0] + tmp[1] + tmp[2], tmp[0] * tmp[1] * tmp[2], tmp[0] + tmp[1] * tmp[2], tmp[0] * tmp[1] + tmp[2], (tmp[0] + tmp[1]) * tmp[2], tmp[0] + tmp[1] * tmp[2], tmp[0] * tmp[1] + tmp[2], tmp[0] * (tmp[1] + tmp[2]))
