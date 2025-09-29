from stats import count_words
from stats import count_characters
from stats import sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
        return file_content
    

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
        
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_dictionary(character_count, character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        char = item.get("char")
        num = item.get("num")
        if not isinstance(char, str) or not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ===============")

main()







