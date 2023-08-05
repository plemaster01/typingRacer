# from nltk.corpus import words

# from nltk import popular
# from nltk.corpus import popular

from nltk.corpus import words
wordlist = words.words()
wordlist.sort(key=len)
file = open('words.txt', 'a')
for word in wordlist:
    if 1 < len(word) < 9:
        file.write(word + '\n')
file.close()