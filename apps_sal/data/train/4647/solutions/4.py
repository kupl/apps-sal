def get_neighbourhood(type_, arr, co):
    h, w = len(arr), len(arr[0])
    i, j = co
    if not arr[0] or i >= h or j >= w:
        return []
    li = []
    if type_ == 'moore':
        return [arr[k][l] for k in range(i - 1 if i > 0 else 0, (i + 1 if i < h - 1 else h - 1) + 1)
                for l in range(j - 1 if j > 0 else 0, (j + 1 if j < w - 1 else w - 1) + 1) if [k, l] != [i, j]]
    else:
        li = [arr[i - 1][j] if i > 0 else 'x',
              arr[i + 1][j] if i < h - 1 else 'x',
              arr[i][j - 1] if j > 0 else 'x',
              arr[i][j + 1] if j < w - 1 else 'x']
        while 'x' in li:
            li.remove('x')
        return li
