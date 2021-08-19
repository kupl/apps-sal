import urllib.request


def get_member_since(username):
    """ this is not a proper solution """
    url = 'https://www.codewars.com/users/' + username + '/stats'
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    return html.split('Member Since')[1][5:13]
