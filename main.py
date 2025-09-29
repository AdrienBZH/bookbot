from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
        return file_content
    

def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    
    print(f"Found {word_count} total words")
    print(f"{character_count}")

main()







