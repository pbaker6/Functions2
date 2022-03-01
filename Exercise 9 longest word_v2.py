# Function to find the longest word(s) in a list, even if more than one
def longest_word(word_list):
    longest = [""]
    for word in word_list:
        if len(word) > len(longest[0]):
            longest = [word]
        elif len(word) == len(longest[0]):
            longest.append(word)
    return longest


# Main routine
words = []
word_ = ""
while word_ != "1":
    word_ = input("Add word to list (or 1 to end): ")
    words.append(word_)

print(f"The longest word/words in the list {words} "
      f"is/are: {longest_word(words)}")


