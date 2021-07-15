def well(arr):
    c = ''.join(map(str,arr)).lower().count('good')
    return ['Fail!','Publish!','I smell a series!'][bool(c)+(c>2)]
