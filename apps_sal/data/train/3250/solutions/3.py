from re import sub


def short_form(s):
    return sub('(?!^)[aeiouAEIOU](?!$)', '', s)
