def my_very_own_split(string, delimiter = None):
    for s in __import__('string').split(string,delimiter): yield s
