def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict_char_count = {}
    
    characters = text.lower()

    for character in characters:
        if character.isalpha():
            if character in dict_char_count:
                character_lowercase = character.lower()
                dict_char_count[character_lowercase] += 1
            else:
                dict_char_count[character] = 1

    return dict_char_count







