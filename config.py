# read text
f = open("lorem_ipsum.txt","r")
test_string = f.read()

# characters
capChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowChars = capChars.lower()
chars = capChars + lowChars

# seperators
seperators = [" ", "\t", "\n",".", ",", ";", ":", "'", "\"", "?", "!", ":"]

testing_string = "ab cd ef"
# sys.path.append(".")??