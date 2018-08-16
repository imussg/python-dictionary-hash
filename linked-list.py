class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
class LettersLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.head.next = None
        self.length = 1
    def __str__(self):
        tempStr = self.head.value
        iter = self.head
        while iter.next != None:
            iter = iter.next
            tempStr += "->" + iter
        return str(tempStr)
    @classmethod
    def add(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
class HashLinkedList:
    def __init__(self):
        self.head = createLettersHash(0)
        self.iter = self.head
        # for charIndex, charArray in vars(self.head).iteritems():
    def hashWord(self, word):
        # charIndex, count updated each loop; next updated so long as word is not at its end
        letter = word[index].lower()
        tempLen = len(word)-1
        if ord(letter) > 96 and ord(letter) < 123:
            self.iter[letter].count += 1
            # if the index is at the last letter in the word in question
            if self.iter[letter].charIndex == tempLen:
                self.iter[letter].isEnd = True
                return
            elif self.iter[letter].next == None:
                self.iter[letter].next = createLettersHash(self.iter[letter].charIndex+1)
            self.iter = self.iter[letter].next
                return hashWord()
def createLettersHash(charIndex):
    # set's up Object whose keys all have Arrays with 2 values: boolean (whether or not a word ends here), and either none(if no words exist beyond here), or another nested version of this
    return {'a':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'b':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'c':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'d':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'e':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'f':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'g':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'h':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'i':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'j':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'k':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'l':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'m':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'n':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'o':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'p':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'q':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'r':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'s':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'t':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'u':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'v':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'w':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'x':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'y':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False},'z':{'next': None, 'charIndex': charIndex, 'count': 0, 'isEnd': False}}
def HashWord(lll, word, iter, index=0):
    letter = word[index].lower()
    tempLen = len(word)-1
    if index == tempLen:
        iter[letter][0] = True
        iter[letter][2] += 1
        return lll
    else:
        # iter = iter[letter].value
        if ord(letter) > 96 and ord(letter) < 123:
            iter[letter][2] += 1
            if iter[letter][1] == None:
                iter[letter][1] = createLettersHash()
            return HashWord(lll, word, iter[letter][1], index+1)
        else:
            return lll
        # return HashWord(lll, word, )
        # iter.value[1] = createLettersHash()
# letterHash = HashWord(letterHash, "hello", letterHash)
letterHash = createLettersHash()
file = open('dictionary.txt', 'r')
words = file.read().split()
file.close()
for word in words:
    print(word)
    # letterHash = HashWord(letterHash, word, letterHash)
# index = 0
# while index < 26:
#     print(letterHash[chr(ord('a')+index)][2])

    # letter = word[0].lower()
    # letter = ord(letter)
    # if letter > 96 and letter < 123:
    #     letterHash = HashWord(letterHash, word, letterHash)
    #     letter = chr(letter)
    #     self.length += 1
# node = Node("first")
# node.next = Node("second")
# print(node)
# print(node.next)