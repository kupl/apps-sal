domain_name=lambda url:url.replace("http://","").replace("www.","").replace("https://","").replace("."," ").split()[0]
