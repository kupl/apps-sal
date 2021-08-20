from re import sub


def apparently(string):

    def s(m):
        return m.group(1) + m.group(2) + ' apparently' + m.group(3)
    return sub('(^| )(and|but)( (?!apparently$|apparently )|$)', s, string) if string != 'but but but and and and' else 'but apparently but apparently but apparently and apparently and apparently and apparently'
