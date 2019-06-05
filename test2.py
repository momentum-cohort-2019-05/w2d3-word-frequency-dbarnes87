import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

f = open("seneca_falls.txt")
text_to_read = (f.read())
lower_case_text = text_to_read.lower()
no_punctation_text = re.sub('[^A-Za-z]', ' ', lower_case_text)
split_word_text = no_punctation_text.split()
list_of_words = []
for word in split_word_text:
    if word not in STOP_WORDS:
        list_of_words.append(word)
# print(list_of_words)

def get_second_item(seq):
    return seq[1]

def print_freq(frequency):
    print("\n\nFrequency\n==========")
    for word, frq in frequency:
        print(word, frq)


def count_freq(list_of_words):

    master_list = {}

    for word in list_of_words:
        if master_list.get(word) == None:
            master_list[word] = 1
        else:
            master_list[word] += 1

    print(master_list)

count_freq(list_of_words)

# def enter_frequency(word_frequency):
#     if word in list_of_words:
#         master_list[word] += 1
#     else:
#         master_list[word] = 1


def print_word_freq(list_of_words):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)










# def most_common(list_of_words):
#     return max(set(list_of_words), key=list_of_words.count)

# print(most_common(list_of_words))