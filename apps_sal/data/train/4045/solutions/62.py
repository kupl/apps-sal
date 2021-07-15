def number(lines):
    line_number = 1
    text_editor = []
    for line in lines:
        text_editor.append(f"{line_number}: {line}")
        line_number += 1
    return text_editor

