
import os

DIR_PATH = os.getcwd()
FILENAME = "input.txt"
FILEPATH = DIR_PATH + "/" + FILENAME

def getIDs(filepath):
    with open(filepath) as f:
        IDs = f.readlines()
    return IDs

#returns true if ID has any letter appearing exactly
#n times in it

def getChecksum(IDs):

    def countLetters(ID, n):
        counts = dict()
        for l in ID:
            counts[l] = counts.get(l, 0) + 1
        return any([v == n for _,v in counts.items() ])

    num_2s, num_3s = zip(*[ (countLetters(ID,2),countLetters(ID,3)) for ID in IDs])
    return num_2s.count(True) * num_3s.count(True)



#PART 2



def getPair(IDs):

    def getNumDifferences(str1, str2):
        return [a != b for a,b in zip(str1,str2)].count(True)

    def getSimilarChars(str1, str2):
        return ''.join([a for a,b in zip(str1, str2) if a == b ])

    previous = []
    for str1 in IDs:
        for p in previous:
            if getNumDifferences(str1, p) == 1:
                #found a match return soln immediately
                return getSimilarChars(p, str1)
        previous.append(str1)
    return None




def test():
    testIDs = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    testIDs2 = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    print(getChecksum(testIDs))
    print(getPair(testIDs2))


IDs = getIDs(FILEPATH)
print("Soln 1: {}".format(getChecksum(IDs)))
print("Soln 2: {}".format(getPair(IDs)))

#print("f: {}, a:{}".format(countLetters("abcdef", 2), False))
#print("f: {}, a:{}".format(countLetters("abcdee", 2), True))
#print("f: {}, a:{}".format(countLetters("acbcdc", 3), True))
#print("f: {}, a:{}".format(countLetters("ababab", 3), True))
#testIDs = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
#print(getChecksum(testIDs))
















































































#end
