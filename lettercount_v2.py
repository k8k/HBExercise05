from sys import argv
import string

script, filename = argv

def lettercount(filename):
    openfile = open(filename)
    filetext = openfile.read().lower()

    counts = [0] * 26

    for char in filetext:
        if ord(char) in range(97,123):
            counts[ord(char) - 97] +=1

    for item in counts:
        print item
            

    openfile.close()


def main():
    lettercount(filename)


if __name__ == "__main__":
    main()
