def hollow_triangle(n):
    total_width = 2 * n - 1
    triangle = ['#'.center(total_width, '_')]
    for i in range(1, total_width-2, 2):
        triangle.append('#{}#'.format('_' * i).center(total_width, '_'))
    triangle.append('#' * total_width)
    return triangle
