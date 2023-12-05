# Verifying alien dictionary

words = ['almond', 'apricot', 'bubble', 'moon', 'notification']
# words = ['apricot', 'almond', 'bubble', 'moon', 'notification']
# words = ['notification', 'apricot', 'bubble', 'moon', 'almond']

alphabetOrder = 'abcdefghijklmnopqrstuvwxyz'

def isLexicographicallyCorrect(words, alphabetOrder):
    if len(words) == 0: return False
    alphabetOrderHashTable = {}
    for alphabetLetter in alphabetOrder:
        alphabetOrderHashTable[alphabetLetter] = len(alphabetOrderHashTable)
    
    for i in range(len(words)):
        if (len(words) <= i + 1): return True
        if (compare(words[i], words[i + 1], alphabetOrderHashTable) == False):
            return False
        
    return True

def compare(wordOne, wordTwo, alphabetOrderHashTable):
    length = min(len(wordOne), len(wordTwo))
    for i in range(length):
        if alphabetOrderHashTable[wordOne[i]] < alphabetOrderHashTable[wordTwo[i]]: return True
        if alphabetOrderHashTable[wordOne[i]] > alphabetOrderHashTable[wordTwo[i]]: return False
    return len(wordOne) <= len(wordTwo)

result = isLexicographicallyCorrect(words, alphabetOrder)
print(result)
