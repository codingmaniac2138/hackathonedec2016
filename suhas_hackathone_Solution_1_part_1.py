"""
PART-I

(i) Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.
C. Append same word equal to number of occurrences in string.
"""


def Play_with_String(input_string, word):
    print input_string

    # Split input string to get individual words
    my_string = input_string.split()

#(A)
# check for number of occurances of the word in list words
    words = []

    for text in my_string:
        if word == text:
            words.append(word)

#(B)
#set the list if word occurs more then once then strip
    stripped_string = []

    if (len(words) > 1):
        my_string=set(my_string)
        my_string.remove(word)
        stripped_string = ' '.join(my_string)

    else:
        #if word occurs only once then directly strip
        my_string.remove(word)
        stripped_string = ' '.join(my_string)
    print stripped_string
#(C)
# add the word to the stripped_string for number of time it has occured

    final_list = stripped_string.split()
    # append the word entered in the stripped list
    for i in words:
        final_list.append(i)

    final_modified_string = ' '.join(final_list)

#DISPLAYING RESULTS ON THE CONSOLE

    print "Count Of The Word is: " , len(words)
    print "The String after word removal:", stripped_string
    print "The Final String is: " , final_modified_string

Play_with_String("hello hello india is my country", "hello")
