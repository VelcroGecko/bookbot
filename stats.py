def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    char_count_dict = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1

    return char_count_dict

def sort_on(dict):
    return dict["num"]


def sorted_dict(unsorted_dict):
    chars_list = []

    for char, count in unsorted_dict.items():
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list


