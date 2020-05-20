# Read a line of input and parse into a list of strings
stringList = input().split(' ')
anagrams = dict()


def sort_string(word):
    letters_of_the_word = []
    final_string = ''
    for letter in word:
        letters_of_the_word.append(letter)
    letters_of_the_word.sort()
    for sorted_letter in letters_of_the_word:
        final_string += str(sorted_letter)
    return final_string


for element in stringList:
    anagrams[sort_string(str(element))] = []
for element in stringList:
    if sort_string(str(element)) in anagrams.keys():
        anagrams[sort_string(str(element))].append(element)


keys = list(anagrams.keys())
keys.sort()
for key in keys:
    print(key + ': ' + str(anagrams[key]))