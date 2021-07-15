def sort_csv_columns(csv_file_content):
    rows = csv_file_content.split('\n')
    titles = rows[0].split(";")
    order = sorted(range(len(titles)), key=lambda k: titles[k].lower())
    newpages = []
    for row in rows:
        newpages.append(';'.join([row.split(";")[c] for c in order]))
    return '\n'.join(newpages)
