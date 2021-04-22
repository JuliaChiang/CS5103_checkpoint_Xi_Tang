f = open("lorem_ipsum.txt","r")
test_string = f.read()


capChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChars = capChars.lower()
chars = capChars + lowChars
print(chars)

seperators = [" ", "\t", "\n",".", ",", ";", ":", "'", "\"", "?", "!", ":"]

def is_word(short_seqs):
    if short_seqs[-1] in seperators:
        return short_seqs[:-1].isalpha()
    else:
        return False

def word_split(text):
    words = []
    word = ''
    if not text:
        return words
    else:
        for ch in text:
            if ch not in seperators:
                word += ch
            elif word:
                words.append(word)
                word = ''
        return words

def text_break(text):
    elements = []
    word = ''
    if not text:
        return elements
    else:
        for ch in text:
            if ch not in seperators:
                word += ch
            elif word:
                elements.append(word)
                elements.append(ch)
                word = ''
        return elements

def word_to_string(arr):
    return ''.join(arr)

def word_replace(text):
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
    count = 0
    for ch in text:
        if ch == "\n":
            count += 1
    return count



print(f"Words count: {word_count(test_string)}" )
print(f"Characters count: {char_count(test_string)}" )
print(f"Lines count: {line_count(test_string)}" )
print(f"New text: {word_replace(test_string)}" )
