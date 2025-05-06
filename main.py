from stats import count_words, count_characters, sort_on, sorted_dict
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("please enter in the format \n Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #book_path = 'books/frankenstein.txt'
    book_path = sys.argv[1]
    frankenstein_contents = get_book_text(book_path)
    num_words = count_words(frankenstein_contents)
    character_dict = count_characters(frankenstein_contents)
    sorted_characters = sorted_dict(character_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
        # Loop through the sorted characters and print only alphabetic ones
    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["num"]
        
        # Only print if the character is alphabetic
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
    

if __name__ == "__main__":
    main()


