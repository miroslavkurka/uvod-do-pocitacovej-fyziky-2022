# distribucia 
#
#
#


def calculate_probability_of_words(my_text):
    # get the probability, P(word)= N of word/all words in text
    text_dict={}
    with open(my_text) as f:
        for line in f: 
            for word in line.split():
                text_dict[word]+=1 
    
    return text_dict

def get_entropy(my_file):


    entropy=0 

    return entropy

