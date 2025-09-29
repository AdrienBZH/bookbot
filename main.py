def count_words(text):
    words = text.split()
    return len(words)


def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
        return file_content
    

def main():
    relative_path = "books/frankenstein.txt"
    book_text = get_book_text(relative_path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")

main()







