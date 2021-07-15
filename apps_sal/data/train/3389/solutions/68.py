import re
def domain_name(url):    
    g = re.sub('((http|https)\:\/\/)?(www.)?', '',url)
    s = re.search('[a-zA-Z0-9-]*.', g)
    
    return s.group()[:-1]
