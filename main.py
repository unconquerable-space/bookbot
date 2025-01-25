from collections import Counter

def get_char_count(text):
    cleaned_text = "".join(c for c in text if c.isalpha())
    return Counter(cleaned_text.lower())

def get_word_count(text):
    return len(text.split())
    
def generate_book_report(bookpath):
    print(f"--- Begin report of {bookpath} ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wc = get_word_count(file_contents)
        print(f"{wc} words found in the document")
        print()
        cc = get_char_count(file_contents)
        for c in cc:
            print(f"The '{c}' character was found {cc[c]} times")
        print("--- End report ---")
    
def main():
    generate_book_report("books/frankenstein.txt")

main()
