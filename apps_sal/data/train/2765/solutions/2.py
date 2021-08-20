from functools import reduce
import re
SIMPLE_SELECTOR_PATTERN = re.compile('[\\s+~>]+|(\\[[^[]+\\]|[#\\.:]?[^[\\s#\\.:+~>]+)')
SPECIFICITY_PATTERN = re.compile('(^#)|(^[\\.\\[:][^:]?)|(^::|^[^#\\.:[])')


def compare(a, b):
    return max((b, a), key=get_specificity)


def get_specificity(selector):
    return reduce(sum_specificities, list(map(simple_selector_to_specificity, get_simple_selectors(selector))))


def sum_specificities(*specificities):
    return list(map(sum, list(zip(*specificities))))


def simple_selector_to_specificity(simple_selector):
    if simple_selector == '*':
        return [0, 0, 0]
    return [1 if x else 0 for x in SPECIFICITY_PATTERN.match(simple_selector).groups()]


def get_simple_selectors(selector):
    return [match.group(1) for match in SIMPLE_SELECTOR_PATTERN.finditer(selector) if match.group(1)]
