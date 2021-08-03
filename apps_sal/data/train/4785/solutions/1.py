from requests import get


def get_member_since(who):
    return get('https://www.codewars.com/users/' + who).text.split('Since:</b>', 1)[1].split('<', 1)[0]
