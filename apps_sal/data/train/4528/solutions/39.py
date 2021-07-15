from collections import OrderedDict

def my_languages(results):
    return [d for d in OrderedDict(sorted(results.items(), key=lambda x: x[1], reverse=True)).keys() if results[d] >= 60]
