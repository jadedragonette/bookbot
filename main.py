def main():
    book_path = "books/frankenstein.txt"
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
        print(f"The {letter} was found {number} times")
    




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    words = path.split()
    return len(words)

def lower_case_everything(path):
    return path.lower()

def get_character_count(path):
    fixed = lower_case_everything(path)
    counter = {}
    for character in fixed:
        if character not in counter:
            counter[character] = 1
        else:
            counter[character] += 1
    return counter

def sort_on(dict):
    return dict["count"]

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