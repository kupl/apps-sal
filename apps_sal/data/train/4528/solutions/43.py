def my_languages(results):
    ordered = sorted([(score, lang) for lang, score in list(results.items())
                     if score >= 60], reverse=True)
    return [lang for score, lang in ordered]

