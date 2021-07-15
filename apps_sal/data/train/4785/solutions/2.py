from requests import get

def get_member_since(username):
    html = get('https://www.codewars.com/users/'+username).text
    return html.split('Since:</b>', 1)[1].split('<', 1)[0]
