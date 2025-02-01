import string

def only_words(string_input):
    
    for punctuation in string.punctuation:
        if punctuation != "'":
            string_input = string_input.replace(punctuation, '')
        
    List_string = string_input.split()
    return List_string


user_input = input('Insert a text: ')

print(only_words(user_input))
