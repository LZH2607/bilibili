def load_text_to_string(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def load_text_to_string_list(file_path, remove_slash_n=True):
    li = []
    with open(file_path, 'r') as file:
        for line in file:
            if remove_slash_n:
                li.append(line.replace("\n", ""))
            else:
                li.append(line)
    return li
