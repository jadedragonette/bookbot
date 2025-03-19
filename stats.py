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