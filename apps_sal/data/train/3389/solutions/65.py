import re
# Use regex to grab domain name
regex_pattern = "(https?:\/\/)?[w]{0,3}\.?([A-Z,a-z,0-9,-]*).*"

def domain_name(url):
    print(url)
    return re.search(regex_pattern, url).group(2)
