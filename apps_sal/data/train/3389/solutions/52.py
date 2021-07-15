def domain_name(url):
    for i in ["https://","http://","www.",".com",".in"]:url=url.replace(i,'')
    return url.replace('.','/').split('/')[0]
