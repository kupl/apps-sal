from difflib import SequenceMatcher


def substring_test(str1, str2):
    return any((x.size > 1 for x in SequenceMatcher(None, str1.lower(), str2.lower()).get_matching_blocks()))
