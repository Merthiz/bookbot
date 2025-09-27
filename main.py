import sys
from stats import count_words, count_caracters, sort_on

try:
    def main():
        filepath = sys.argv[1]
        print("="* 20 + f" Book report of: {filepath} " + "="* 20)
        words = count_words(filepath)
        letters = count_caracters(filepath)
        print("="* 25 + f" Found {words} total words " + "="* 25)
        ordened_list = sort_on(letters)
        print("="* 29 + f" Characters count: " + "="* 28)
        for item in ordened_list:
            char = item['char']
            num = item['num']
            
            if char.isalpha():
                print(f"{char}: {num}")
                
    main()
    print("="* 80)
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)