def isWhiteSpace(character):
    return character == ' ' or character == '\n'

def slice(sentence):
    words = []
    beginningOfWord = 0
    currentCharacter = 0
    for character in sentence: #character is being defined here
        if isWhiteSpace(character):
            word = sentence[beginningOfWord:currentCharacter]
            words.appen(word.lower())
            beginningOfWord = currentCharacter + 1
        elif currentCharacter == len(sentence) -1:
            word = sentence[beginningOfWord:len(sentence)]
            words.appen(word.lower())
            currentCharacter += 1
        return words

def countWords(sentence):
    wordCount = {} #creating dictionary
    words = slice(sentence)
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    print wordCount

countWords("Hello this is my sentence sentence is my word hello ")
