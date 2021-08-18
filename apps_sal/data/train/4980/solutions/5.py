from csv import reader


def sort_csv_columns(csv_file_content):
    return '\n'.join(map(';'.join, zip(*sorted(zip(*reader(csv_file_content.split('\n'), delimiter=";")), key=lambda x: x[0].lower()))))
