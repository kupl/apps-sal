from operator import itemgetter


def my_languages(results):
    return [language for language, score in sorted(results.items(),key=itemgetter(1), reverse=True) if score >= 60]
