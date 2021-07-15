def well(x):
    d = {i:x.count(i) for i in x}
    if not d.get('good'):
        return 'Fail!'
    elif 1 <= d.get('good') <=2:
        return 'Publish!'
    else:
        return 'I smell a series!'
