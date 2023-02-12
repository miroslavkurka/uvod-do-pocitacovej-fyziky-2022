def count_words_in_text(text_file):
    """
    Count the frequency of each word in a text file.

    Parameters:
    text_file (str): The path to the text file.

    Returns:
    dict: A dictionary where the keys are the words in the text file and the values are their frequency.
    """
    # Open the file
    f = open(text_file, "r")

    text = f.read()
    f.close()

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def calculate_text_entropy(text_file):
    """
    Calculate the entropy of the words in a text file.

    Parameters:
    text_file (str): The path to the text file.

    Returns:
    float: The entropy of the words in the text file.
    """

    word_count = count_words_in_text(text_file)

    entropy = 0
    for word in word_count:
        p = word_count[word] / len(words)
        entropy -= p * math.log2(p)

    print(entropy)


calculate_text_entropy("sherlockholmes.txt")
