import os
from itertools import cycle

DIR_PATH = os.getcwd()
FILENAME = "input.txt"
FILEPATH = DIR_PATH + "/" + FILENAME

#get frequencies from file and add to array
def get_frequencies(filePath):
    fs = []

    with open(filePath) as frequencies:
        for f in frequencies:
            fs.append(int(f))

    return fs

#given an array of frequencies, cycles through until
#it finds repeated frequency
def get_repeated(frequencies):
    curr = 0
    past_fs = set()
    for f in cycle(frequencies):
        curr += f
        if curr in past_fs:
            break
        else:
            past_fs.add(curr)
    return curr


#print(get_repeated([1, -2, 3, 1])) #2

repeated_f = get_repeated(get_frequencies(FILEPATH))
print(repeated_f)






















#end
