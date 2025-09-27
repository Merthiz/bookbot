import sys
from stats import count_words, get_book_text, count_caracters, sort_on

try:
    def main():
        filepath = sys.argv[1]
        print(f"Book report of :{filepath}")
        words = count_words(filepath)
        letters = count_caracters(filepath)
        print(f"Found {words} total words")
        ordened_list = sort_on(letters)
        print("\nCharacters count:")
        for item in ordened_list:
            char = item['char']
            num = item['num']
            
            if char.isalpha():
                print(f"{char}: {num}")
    main()
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)