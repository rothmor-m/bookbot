def main():
#
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)     
    occur = occurence(text)
    ls_dict =[]
    ls_dict.append(occur)
    print(ls_dict)
    

    #print(occur)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    #for key, value in ls_dict:
        #print(f"The {key} character was found {value} times")
    #print(f"The {ls_dict} character was found XXXX times")

    print("--- End report ---")

#create list of dict of alphabet
def dictionary(occur):
    ls_dict = []
    for key, value in occur.items():
        if key.isalpha():
            ls_dict.append(key)
    
    return ls_dict

# split --> creates list of words from text and returns how many characters there are
def count_words(text):
    words = text.split()
    return  len(words)

# count the occurence of each character
def occurence(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# open creates connection to the text in variable f
# read --> reads actual text   
def get_book_text(path):
    with open(path) as f:
        return f.read() 

if __name__=="__main__":
    main()



#do this with more than one book
#
#if we have a list with book_titles
#def main():
#for title in titles:
#book_path = "books/" + title + ".txt"
#text = get_book_text(book_path)
#print(text)