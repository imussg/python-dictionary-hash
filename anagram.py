# this will run the anagram word finding program
import random
from '' import LettersLinkedList
file = open('src/dictionary.txt', 'r')
words = file.read().split()
lettersArray = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
print ord('a')
print ord('z')
for word in words:
    letter = word[0].lower()
    letter = ord(letter)
    if letter > 96 and letter < 123:
        letter = chr(letter)
        lettersArray[letter] += 1
print lettersArray
file.close()
# class wordHash:
#     def __init__(self, words):
        