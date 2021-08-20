import re


def rake_garden(g):
    return re.sub('\\b(?!gravel|rock\\b)\\w+', 'gravel', g)
