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
  return "".join(pol_to_eng.get(c) or c for c in s)
