def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words():
    words = get_book_text.split()
    print(words + 1)
