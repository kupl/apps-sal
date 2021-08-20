import re


def bucket_of(said):
    return {0: 'air', 1: 'water', 2: 'slime', 3: 'sludge'}[bool(re.search('(?i)(water|wet|wash)', said)) + bool(re.search("(?i)(I don't know|slime)", said)) * 2]
