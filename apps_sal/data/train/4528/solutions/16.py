def my_languages(results):
    return [_[0] for _ in sorted([_ for _ in list(results.items()) if _[1] >= 60], key=lambda _: _[1], reverse=True)]

