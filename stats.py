def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    book = get_book_text(text)
    words = len(book.split())
    return words

def count_caracters(text):
    texto = get_book_text(text).lower()
    dictionary = {}
    for letter in texto:
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary

def get_num(dict):
    return dict["num"]

def sort_on(dict):
    dict_list = []
    for char, num in dict.items():
        dict_list.append({"char": char, "num": num})
    dict_list.sort(reverse=True, key=get_num)
    return dict_list