def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words():
    book_path = "books/frankenstein.txt"
    words = book_path.split(" ")
    print(words)


main()
