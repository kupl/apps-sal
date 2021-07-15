def domain_name(url):
    a=url.replace('http:',' ').replace('https:',' ').replace('/',' ').replace('//',' ').replace('.',' ').replace('www',' ').split()
    return(a[0])
