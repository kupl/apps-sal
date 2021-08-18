def solution(string, markers):
    content = string.split("\n")

    clean_content = []
    for full_line in content:

        clean_line = ""
        for char in full_line:

            if not char in markers:
                clean_line += char
            else:
                break

        clean_line = clean_line.strip()

        clean_content.append(clean_line)

    return "\n".join(clean_content)
