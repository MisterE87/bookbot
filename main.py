import sys
from stats import get_num_words, count_characters,sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_output(path_to_file,wordcount,sortedDictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for ch in sortedDictionary:
        if ch["char"].isalpha():
            print(f"{ch["char"]}: {ch["num"]}")
    print("============= END ===============")
    return None

def main():
    if len(sys.argv)<2:
        print("Please run the script providing also the path to the file, ie")
        print('Usage: python3 main.py <path_to_book>')
        #return None
    else:
        path_to_file = sys.argv[1]
        
    booktext = get_book_text(path_to_file)
    wordcount = get_num_words(booktext) 
    #print(f"{wordcount} words found in the document")
    characterdictionary = count_characters(booktext)
    
    sortedDicationary = sort_dictionary(characterdictionary)
    print_output(path_to_file,wordcount,sortedDicationary)
main()
