user_input = input("Please Enter your Text: ")

sentences = user_input.count(".") + user_input.count("!") + user_input.count("?") + user_input.count(";")
words = user_input.count(" ")
characters = len(user_input)


def count_letters(letters):
    return len([x for x in letters if x.isalpha()])


print("Number of Sentences: ", sentences)
print("Number of Words: ", words + 1)
print("Number of Letters: ", count_letters(user_input))
print("Number of Characters: ", characters)
