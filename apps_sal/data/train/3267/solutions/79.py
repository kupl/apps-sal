def well(x):
    count_ = x.count('good')
    return 'Fail!' if count_ == 0 else ('Publish!' if count_ <= 2 else ('I smell a series!'))
