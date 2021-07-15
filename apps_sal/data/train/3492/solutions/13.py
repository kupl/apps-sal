def correct_polish_letters(str_: str) -> str:
    """ Change the letters with diacritics. """
    return str_.translate(
        str.maketrans(
            {
                "ą": "a",
                "ć": "c",
                "ę": "e",
                "ł": "l",
                "ń": "n",
                "ó": "o",
                "ś": "s",
                "ź": "z",
                "ż": "z"
            }
        )
    )
