import config
text = config.test_string
chars = config.chars
seperators = config.seperators


def is_word(short_seqs):
    if not short_seqs:
        return False
    for i in short_seqs:
        if i in seperators:
            return False
    return True

def has_seperators(text):
    for i in text:
        if i in seperators:
            return True
    return False

def find_sep_index(text):
    length = len(text)
    for i in range(length):
        if text[i] in seperators:
            return i
    return None

def has_new_line(text):
    for i in text:
        if i == "\n":
            return True
    return False

def count_new_line(text):
    count = 0
    length = len(text)
    for i in range(length):
        if text[i] == "\n":
            count += 1
    return count

def word_split(text):
    elements = []
    if not text:
        return elements
    elif text in seperators:
        return elements

    if is_word(text):
        elements.append(text)
        return elements
    elif has_seperators(text):
        sep_index = find_sep_index(text)
        if sep_index == 0:
            return word_split(text[1:])
        if sep_index == len(text)-1:
            return word_split(text[:-1])
        else:
            return word_split(text[:sep_index])+word_split(text[sep_index+1:])

def text_break(text):
    elements = []
    if not text:
        return elements
    elif is_word(text):
        elements.append(text)
        return elements
    elif text in seperators:
        elements.append(text)
        return elements
    elif has_seperators(text):
        sep_index = find_sep_index(text)
        front = text_break(text[:sep_index])
        tail = text_break(text[sep_index+1:])
        return front + [text[sep_index]] + tail

def word_to_string(arr):
    return ''.join(arr)

def word_replace(text):
    print(text)
    target_word = input("Replace:")
    new_word = input("Replace by:")
    arr = text_break(text)
    length = len(arr)
    for i in range(length):
        if arr[i].lower() == target_word.lower():
            arr[i] = new_word
    new_text = word_to_string(arr)
    return new_text


def word_count(text):
    words = word_split(text)
    words = set(words)
    return len(words)

def char_count(text):
    count = 0
    for ch in text:
        if ch not in seperators:
            count += 1
    return count

def line_count(text):
    if not text:
        return 0
    if not has_new_line(text):
        return 1
    else:
        count = count_new_line(text) + 1
        return count

