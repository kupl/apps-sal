import re

def rake_garden(garden):
    return re.sub(r'(?<!\S)(?!gravel|rock)\S+', 'gravel', garden)
