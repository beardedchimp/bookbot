from operator import itemgetter

def get_word_count(book_string):
    words = book_string.split()
    num_words = len(words)
    return num_words

def get_char_breakdown(book_string):
    char_dict = {}

    for char in book_string:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sorted_list(char_dict):
    list_of_dict = []
    for key in char_dict:
        if key.isalpha():
            count = {}
            count["char"] = key
            count["num"] = char_dict[key]
            list_of_dict.append(count)
    
    list_sorted = sorted(list_of_dict,key=itemgetter('num'),reverse=True)
    return list_sorted