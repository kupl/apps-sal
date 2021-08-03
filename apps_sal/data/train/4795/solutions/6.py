import re


def flesch_kincaid(text):
    words = len(text.split())
    syllables = len(re.findall('[aeiou]+', text.lower()))
    sentences = len(re.split('[.!?]+', text.strip('.!?')))

    return round(0.39 * words / sentences + 11.8 * syllables / words - 15.59, 2)
