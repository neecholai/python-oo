"""WordFinder: counts all words in a file and can return a random word from that file.
SpecialWordFinder is the same as WordFinder but ignores commented out lines"""
from random import choice


class WordFinder:
    """Opens file and stores list of words in file.
    random() method returns random word from the list of words.
    """

    def __init__(self, file):
        "Call read_file method and print number of words read in the file."
        self.read_file(file)
        self.file_location = file
        print(f"{len(self.words)} words read")

    def __repr__(self):
        return f"<{len(self.words)} words in file, {self.file_location}. Find something random, baby.>"

    def read_file(self, file):
        "Reads file and creates list of words in file."
        self.file = open(file)
        self.words = []
        for line in self.file:
            words_in_line = [word.strip('\n') for word in line.split()]
            self.words.extend(words_in_line)
        self.file.close()

    def random(self):
        "Returns random word from list of words in file."
        random_word = choice(self.words)
        print("random word :", random_word)
        return random_word


word_finder_test = WordFinder("words.txt")
word_finder_test.random()

# class WordFinderAlt:
#     """Opens file and stores list of words in file.
#     random() method returns random word from the list of words.
#     """

#     def __init__(self, file):
#         "Call read_file method and print number of words read in the file."
#         self.words = []
#         self.read_file(file)
#         self.file_location = file
#         print(f"{len(self.words)} words read")

#     def __repr__(self):
#         return f"<{len(self.words)} words in file, {self.file_location}. Find something random, baby.>"

#     def parse_line(self, lines):
#         "Reads lines in file and creates list of words in file."
#         for word in lines:
#             words_in_line = [word.strip('\n') for word in line.split()]
#             self.words.extend(words_in_line)

#     def parse_file(self, file):
#         "Reads file and creates list of lines from file."
#         self.file = open(file)
#         lines = []
#         for line in self.file:
#             lines.append(line)
#         self.file.close()
#         return lines

#     def random(self):
#         "Returns random word from list of words in file."
#         random_word = choice(self.words)
#         print("random word :", random_word)
#         return random_word


# word_finder_test = WordFinder("words.txt")
# word_finder_test.random()


class SpecialWordFinder(WordFinder):
    """Opens file and stores list of words in file. Ignores commented out lines.
    random() method returns random words from the list of words.
    """

    def read_file(self, file):
        "Reads file and creates list of words in file. Ignores commented out lines."
        self.file = open(file)
        self.words = []

        for line in self.file:
            hashtag_index = line.find("#")
            if hashtag_index > -1:
                line = line[:hashtag_index]
            words_in_line = [word.strip('\n') for word in line.split()]
            self.words.extend(words_in_line)

        self.file.close()


special_word_finder_test = SpecialWordFinder("words.txt")
special_word_finder_test.random()
