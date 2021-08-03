from operator import itemgetter


def my_languages(results):
    return [lang for lang, score in sorted(results.items(), key=itemgetter(1), reverse=True) if score >= 60]
