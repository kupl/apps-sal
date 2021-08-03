def format_words(words):
    # reject falsey words
    if not words:
        return ""

    # ignoring empty strings
    words = [word for word in words if word]

    number_of_words = len(words)
    if number_of_words <= 2:
        # corner cases:
        # 1) list with empty strings
        # 2) list with one non-empty string
        # 3) list with two non-empty strings
        joiner = " and " if number_of_words == 2 else ""
        return joiner.join(words)

    return ", ".join(words[:-1]) + " and " + words[-1]
