import re


def rake_garden(garden):
    return re.sub('(?<!\\S)(?!gravel|rock)\\S+', 'gravel', garden)
