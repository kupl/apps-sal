import re


def domain_name(url):
    pattern = "[\-\.a-z0-9]+|www.[\-a-z0-9]+\."
    string = re.findall(pattern, url)
    string = string[1 if len(string) > 1 and 'http' in string[0] else 0]

    return re.sub("www\.|\/\/|\.[\.a-z]+$|\.", "", string)
