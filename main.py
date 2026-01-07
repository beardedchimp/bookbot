import sys
from stats import get_word_count, get_char_breakdown, sorted_list


# Takes in a text file and returns a string
def get_book_text(book_filepath):
    with open(book_filepath) as f:
        book_string = f.read()
    
    return book_string


# Main function that runs
def main():
    
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        num_words = get_word_count(book_text)
        char_breakdown = get_char_breakdown(book_text)
        char_sorted_list = sorted_list(char_breakdown)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in char_sorted_list:
        print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")



main()
