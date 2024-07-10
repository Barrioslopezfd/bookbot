def main():
    with open("books/frankestein.txt") as f:
        franken = f.read().lower()
        word_count = franken.split()
        copy = dict.fromkeys(set(franken[:]), 0)
        print(copy)
main()
