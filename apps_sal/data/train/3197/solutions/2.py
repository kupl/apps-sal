personal_suffixes = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"],
}


def conjugate(verb):
    base, group = verb[:-2], verb[-2:]
    suffixes = personal_suffixes[group]
    return {verb: [f"{base}{suffix}" for suffix in suffixes]}
