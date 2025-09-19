def get_num_words(bookfile):
    return len(bookfile.split())

def count_characters(bookfile):
    lowercasebookfile = list(bookfile.lower())
    characterdictionary = {}
    
    for character in lowercasebookfile:
        if character in characterdictionary:
            characterdictionary[character] += 1
        else:
            characterdictionary[character] = 1
            
    return characterdictionary

def sort_dictionary(characterdictionary):
    dictList = []
    for character,count in characterdictionary.items():
        dictList.append({"char": character, "num": count})

    dictList.sort(reverse=True,key=sort_on)
    return dictList

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]