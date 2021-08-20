def sort_csv_columns(csv_file_content):
    table = sorted(zip(*(row.split(';') for row in csv_file_content.split('\n'))), key=lambda col: col[0].lower())
    return '\n'.join((';'.join(row) for row in zip(*table)))
