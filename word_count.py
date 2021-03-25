f = open("lorem_ipsum.txt","r")
test_string = f.read()


capChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChars = capChars.lower()
chars = capChars + lowChars
print(chars)

seperators = [" ", "\t", "\n"]

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

def word_count(text):
    words = word_split(text)
    return len(words)

def char_count(text):
    count = 0
    for ch in text:
        if ch not in seperators:
            count += 1
    return count

print(word_count(test_string))
print(char_count(test_string))
