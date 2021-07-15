import string
def sort_csv_columns(csv_file_content):
    orderby=' _0123456789'+string.ascii_lowercase
    l=list(zip(*[i.split(';') for i in csv_file_content.split('\n')]))
    l.sort(key=lambda a:[orderby.index(i) for i in a[0].lower()])
    return '\n'.join(';'.join(i) for i in zip(*l))
