def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    chars = {}
    string = text.lower()

    for c in string:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    print(chars)
    
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
