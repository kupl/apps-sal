def sorter(textbooks):
    obj = {}
    lower_case_textbooks = []
    for textbook in textbooks:
        lower_case_textbook = textbook.lower()
        obj[lower_case_textbook] = textbook
        lower_case_textbooks.append(lower_case_textbook)
    sorted_textbooks = sorted(lower_case_textbooks)
    output_list = []
    for sorted_textbook in sorted_textbooks:
        output_list.append(obj[sorted_textbook])
    return output_list
