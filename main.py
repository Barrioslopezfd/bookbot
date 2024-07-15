def main():
     book = frankestein()
     words = word_count(book) 
     chars = char_count(book)
     report_generator(words, chars)

def frankestein():
    with open("books/frankestein.txt") as f:
        return f.read()

def word_count(foo):
   return len(foo.split())

def char_count(book):
    book = book.lower()
    copy = dict.fromkeys(set(book[:]), 0)
    for f in book:
        copy[f] += 1
    return copy

def sort_on(dict):
    return dict["num"]

def report_generator(words, chars):
    list = []
    for c in chars:
        if c.isalpha():
            list.append(dict(char=c, num=chars[c]))
    list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for l in list:
        print(f"The {l['char']} character was found {l['num']} times")
    print("--- End report ---")

main()