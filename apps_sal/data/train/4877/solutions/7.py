import itertools as it

def love_language(partner, weeks):
    for lang in it.cycle(LOVE_LANGUAGES):
        if partner.response(lang) == "positive":
            if partner.response(lang) == "positive":
                if partner.response(lang) == "positive":
                    return lang
