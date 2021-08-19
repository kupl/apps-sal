def segment_display(num):
    segs = ' \n ### |     | ### | ### |     | ### | ### | ### | ### | ### \n#   #|    #|    #|    #|#   #|#    |#    |    #|#   #|#   #\n#   #|    #|    #|    #|#   #|#    |#    |    #|#   #|#   #\n#   #|    #|    #|    #|#   #|#    |#    |    #|#   #|#   #\n     |     | ### | ### | ### | ### | ### |     | ### | ### \n#   #|    #|#    |    #|    #|    #|#   #|    #|#   #|    #\n#   #|    #|#    |    #|    #|    #|#   #|    #|#   #|    #\n#   #|    #|#    |    #|    #|    #|#   #|    #|#   #|    #\n ### |     | ### | ### |     | ### | ### |     | ### | ### '
    numbers = {str(i): [] for i in range(10)}
    for s in segs.split('\n')[1:]:
        for (i, t) in enumerate(s.split('|')):
            numbers[str(i)].append(t)
    numbers[' '] = ['     '] * 9
    return '\n'.join(['| ' + ' | '.join([numbers[ch][y] for ch in f'{num:>6}']) + ' |' for y in range(9)])
