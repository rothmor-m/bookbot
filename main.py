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



#do this with more than one book
#book_path = "books/" + title + ".txt"
#if we have a list with book_titles
#def main():
#for title in titles:
#book_path = "books/title.txt" --> does that work? because the titles in the list dont have txt ??
#text = get_book_text(book_path)
#print(text)