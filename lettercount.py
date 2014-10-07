from sys import argv
import string

script, filename = argv

def lettercount(filename):
    openfile = open(filename)
    filetext = openfile.read().lower()

    letters = []
    counts = []

    for char in filetext:
        if char in string.ascii_lowercase:
            if char in letters:
                counts[letters.index(char)] += 1
            else:
                letters.append(char)
                counts.append(1)
        else:
            del char

    tuple_list = sorted(zip(letters,counts))
    
    for item in tuple_list:
        print "There are", item[1], "instances of", item[0]

    openfile.close()


def main():
    lettercount(filename)


if __name__ == "__main__":
    main()
