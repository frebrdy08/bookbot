def main():

    book_path = "books/frankenstein.txt"
    text_of_book = get_book_text(book_path)
    characters = character_count(text_of_book)
    num_words = get_num_words(text_of_book)
    full_report = get_report(characters, num_words, book_path)
    print(full_report)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def character_count(text):
    character_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def split_dict(dict):
    out_list = [{"character": key, "count": value} for key, value in dict.items()]
    return out_list

def sort_on(dict):
    return dict["count"]

def filter_list(char_dict):
    char_list = split_dict(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    alpha_list = [char_dict for char_dict in char_list if char_dict["character"].isalpha()]
    return alpha_list

def get_report(char_dict, num_words, book_path):
    filtered_chars = filter_list(char_dict)
    output_string = f"---Begin report of {book_path} ---\n"
    output_string += f"{num_words} words found in the document \n\n"
    for mini_dict in filtered_chars:
        character = mini_dict["character"]
        count = mini_dict["count"]
        output_string += f"The '{character}' character was found {count} times\n"
    output_string += "--- End Report ---"
    return output_string

main()
