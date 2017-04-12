# Mr. Smith  in between the sentence is not tokenized
# Dot space and caps letter is only recognized
# Dot Space and small letter is not recognized

from nltk.tokenize import sent_tokenize, word_tokenize

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."

phrases = sent_tokenize(data)
words = word_tokenize(data)

print(phrases)
print(words)