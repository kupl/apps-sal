def longest_slide_down(a):
    a = a[::-1]
    for j in range(1, len(a)):
        a[j] = [a[j][i] + max(a[j - 1][i], a[j - 1][i + 1]) for i in range(len(a[j]))]
    return a[-1][0]
