from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_key = make_the_dictionary(character_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in sorted_key:
        letter = item["character"]
        number = item["count"]
        print(f"{letter}: {number}")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def make_the_dictionary(dict):
    sorted = []
    final = []
    for item in dict:
        good = {}
        if item.isalpha():
            good["character"] = item
            good["count"] = dict[item]
            sorted.append(good)
            sorted.sort(reverse=True, key=sort_on)
    return sorted





main()