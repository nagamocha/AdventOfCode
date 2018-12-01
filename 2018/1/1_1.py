import os

DIR_PATH = os.getcwd()
FILENAME = "input.txt"

def get_frequencies(filePath):
    with open(filePath) as frequencies:
        final_frequency = 0
        for f in frequencies:
            final_frequency += int(f)
    return final_frequency

final_frequency = get_frequencies(DIR_PATH + "/" + FILENAME)

print(final_frequency)










































#end
