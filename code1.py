# Sentiment-Classifier
# Python Functions, Files, and Dictionaries - Final Course Project - Project - Part 1: Sentiment Classifier

# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the numberof  # retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files
# positive_words.txt and negative_words.txt.

# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the 
# Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the 
# tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.



# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from 
# everywhere in the word. (Hint: remember the .replace() method for strings.)



#-------------------------------------------------------------------------------------------------------------------------
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word): #word is a string
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word
    
#----------------------------------------------------------------------------------------------------------------------------


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word): #word is a string
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:                   #reading line-by-line from the .txt file
        if lin[0] != ';' and lin[0] != '\n': #just print the lin , you will get the ans , why did they use this condition
            positive_words.append(lin.strip())

def get_pos(txt): #txt is string of one or more sentnces
    txt = txt.lower() #Condition given in question
    lst = txt.split() #list of words
    count_of_pos_words = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in positive_words:
            count_of_pos_words += 1
    return count_of_pos_words         #count of postive words present in txt string
    
#-------------------------------------------------------------------------------------------------------------------------------
  #this is same as above for negative words  
    
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word): #word is a string
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
            
def get_neg(txt): #txt is string of one or more sentnces
    txt = txt.lower() #Condition given in question
    lst = txt.split() #list of words
    count_of_neg_words = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in negative_words:
            count_of_neg_words += 1
    return count_of_neg_words

#-------------------------------------------------------------------------------------------------------------------------


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word): #word is a string
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(txt): #txt is string of one or more sentnces
    txt = txt.lower() #Condition given in question
    lst = txt.split() #list of words
    count_of_neg_words = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in negative_words:
            count_of_neg_words += 1
    return count_of_neg_words

def get_pos(txt): #txt is string of one or more sentnces
    txt = txt.lower() #Condition given in question
    lst = txt.split() #list of words
    count_of_pos_words = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in positive_words:
            count_of_pos_words += 1
    return count_of_pos_words         #count of postive words present in txt string
    

    
output_file = open("resulting_data.csv","w")
output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
output_file.write('\n')
    
with open("project_twitter_data.csv", 'r') as connection_file:
    lines = connection_file.readlines() #list of data of each line in .csv file
    #print(lines)
    #header = lines[0]
    #field_names = header.strip().split(',')
    #print(field_names)
    for line in lines[1:]:
        vals = line.strip().split(',') #list each line data
        row_string = '{},{},{},{},{}'.format(vals[1], vals[2], get_pos(vals[0]), get_neg(vals[0]), get_pos(vals[0])-get_neg(vals[0]))
        output_file.write(row_string)
        output_file.write('\n')

output_file.close()
