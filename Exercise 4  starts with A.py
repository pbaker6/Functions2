# Function to check if a word starts with 'A'
def starts_with_a(word_):
    if word_[0] == "A":
        return True
    else:
        return False


# Main routine
word = input("Enter the word: ").title()
print(starts_with_a(word))

