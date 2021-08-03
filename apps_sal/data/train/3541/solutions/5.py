def find_page_number(pages):
    result = []
    for j, page in enumerate(pages):
        if page != j - len(result) + 1:
            result.append(page)

    return result
