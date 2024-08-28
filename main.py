def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

def count_words(text):
    words = text.split()
    return  len(words)
    
def get_book_text(path):
    with open(path) as f:
        return f.read() 

if __name__=="__main__":
    main()



