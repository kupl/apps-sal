def contamination(text, char):
    if text == '' or char == '':
        return ''
    else:
        ans = ''
        for i in text:
            ans = ans + char
        return ans
