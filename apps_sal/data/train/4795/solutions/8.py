import re


def flesch_kincaid(text):
    words = len(re.findall("\w+", text))
    syl = len(re.findall("[aeiou]+", text, re.I))
    sen = len(re.findall("[\w\s]+", text))
    res = (0.39 * words / sen) + (11.8 * syl / words) - 15.59
    return round(res * 100) / 100.0
