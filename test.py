import re

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

f = open("seneca_falls.txt")
text_to_read = (f.read())
lower_case_text = (text_to_read.lower())
no_punctation_text = re.sub('[^A-Za-z]', ' ', lower_case_text)
split_word_text = no_punctation_text.split()
# remove_stop_words = [word for word in split_word_text if word not in STOP_WORDS]
list_of_words = []
for word in split_word_text:
    if word not in STOP_WORDS:
        list_of_words.append(word)
print(list_of_words)
# def most_common(list_of_words):
#     return max(set(list_of_words), key=list_of_words.count)

# print(most_common(list_of_words))

# file = "seneca_falls.txt"

# def print_word_freq(file):
    # """Read in `file` and print out the frequency of words in that file."""
#     pass    

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)




# # words = list_of_words
# # various_words = sorted(words, key=len)

# # print(various_words)




















# # all_letters = "abcdefghijklmnopqrstuvwxyz"
# # found_letters = []
# # for letter in persons_phrase.lower():
# #     if letter in all_letters:
# #         found_letters.append(letter)
