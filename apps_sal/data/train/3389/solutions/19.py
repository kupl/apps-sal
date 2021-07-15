import re
def domain_name(url):
   return re.sub(r'(http(s)?:\/\/)?(www\.)?',"",url).split(".")[0]
