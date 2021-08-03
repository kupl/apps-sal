def frame(text, char):
    text_lens = [len(x) for x in text]
    longest_len = max(text_lens)
    frame_list = [char * (longest_len + 4)]
    for str in text:
        frame_list.append("{} {}{} {}".format(char, str, " " * (longest_len - len(str)), char))
    frame_list.append(char * (longest_len + 4))
    return "\n".join(frame_list)
