def remove_duplicate_words(x):
    a=''
    for i in x.split():
        if i not in a:
            a+=i +' '
    return a[:-1]
