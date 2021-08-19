def well(a):
    return ['Fail!', 'Publish!', 'I smell a series!'][min((a.count('good') + 1) // 2, 2)]
