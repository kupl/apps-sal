from typing import List, Tuple
from urllib.parse import urlparse
import re


def generate_bc(url: str, separator: str) -> str:
    # print(f'url = {repr(url)}')
    # print(f'separator = {repr(separator)}')

    home_url = '<a href="/">HOME</a>'  # type: str

    (path_components, last_path) = split_url(url)
    if last_path.startswith("index."):
        last_path = ''

    last_path = re.sub(r"(.html|.htm|.php|.asp)$", "", last_path)

    if not path_components:  # empty
        if not last_path:
            return '<span class="active">HOME</span>'
    elif not last_path:
        last_path = path_components.pop()

    return separator.join([
        home_url, *generate_bc_middle(path_components),
        generate_bc_last(last_path)
    ])


def generate_bc_middle(path_components: List[str]) -> List[str]:
    # return ['<a href="/important/">IMPORTANT</a>', '<a href="/important/confidential/">CONFIDENTIAL</a>']
    cumulative_path = ''
    result: List[str] = []
    for path in path_components:
        cumulative_path = (cumulative_path + '/' +
                           path) if cumulative_path else path
        bc = path.replace('-',
                          ' ').upper() if len(path) <= 30 else acronymyze(path)
        result.append(f'<a href="/{cumulative_path}/">{bc}</a>')
    return result


def acronymyze(long_word: str) -> str:
    """ Shorten it, acronymizing it
    (i.e.: taking just the initials of every word) """
    ignore_words = [
        "the", "of", "in", "from", "by", "with", "and", "or", "for", "to",
        "at", "a"
    ]
    return ''.join(word[0].upper() for word in long_word.split('-')
                   if word not in ignore_words)


def generate_bc_last(last_path: str) -> str:
    if len(last_path) > 30:
        bc = acronymyze(last_path)
    else:
        bc = last_path.replace('-', ' ').upper()
    return f'<span class="active">{bc}</span>'


def split_url(url: str) -> Tuple[List[str], str]:
    """ Returns a tuple by splitting the given url
    url = 'mysite.com/years/pictures/holidays.html'
    returns a tuple ([years,pictures], 'holidays.html')
    """

    # Example url = 'https://mysite.com/years/pictures/holidays.html'
    parse_result = urlparse(url)
    # ParseResult(scheme='https', netloc='mysite.com', path='/years/pictures/holidays.html',
    #               params='', query='', fragment='')

    # urlparse recognizes a netloc only if it is properly introduced by ‘//’.
    # Otherwise the input is presumed to be a relative URL and thus to start
    # with a path component.

    # Redo urlparse to make sure that parse_result.path has only filepath and not hostpath part
    if not parse_result.scheme and not url.startswith('//'):
        parse_result = urlparse('//' + url)

    if not parse_result.path:  # empty path
        path_components = []
        last_path = ''
    elif parse_result.path.startswith('/'):
        path_components = [
            component for component in parse_result.path.split("/")
        ]
        path_components.pop(0)  # Remove ''
        # ['', 'years', 'pictures', 'holidays.html']
        last_path = path_components.pop()  # type: str
    else:
        raise Exception("Invalid url")

    # (['years', 'pictures'], 'holidays.html')
    return (path_components, last_path)

