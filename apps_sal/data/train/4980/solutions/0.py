def sort_csv_columns(csv_file_content, sep=';', end='\n'):
    '''Sort a CSV file by column name.'''
    csv_columns = zip(*(row.split(sep) for row in csv_file_content.split(end)))
    sorted_columns = sorted(csv_columns, key=lambda col: col[0].lower())
    return end.join(sep.join(row) for row in zip(*sorted_columns))
