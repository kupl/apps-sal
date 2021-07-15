def remove_url_anchor(url):
    j = 0
    for i in url:
        j +=1
        if i == '#':
            print(j)
            url = url[0:(j-1)]
            return url
        else:
            pass
    return url
        

