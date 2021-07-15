import re

def correct_polish_letters(s):
    pol_to_eng = {
      "ą": "a",
      "ć": "c",
      "ę": "e",
      "ł": "l",
      "ń": "n",
      "ó": "o",
      "ś": "s",
      "ź": "z",
      "ż": "z",
    }
    return re.sub(
        r"[ąćęłńóśźż]",
        lambda matchobj: pol_to_eng[matchobj.group()],
        s
    )
