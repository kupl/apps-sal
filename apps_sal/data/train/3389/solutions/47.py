from urllib.parse import urlparse

def domain_name(url):
    url = url.replace("www.","")
    url = url.replace("http://","")
    url = url.replace("https://","")
    domain_name = url.split('.')[0]
    return(domain_name)
            
            

