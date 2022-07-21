# Read the file and save it to a variable
file = open("make_me_a_video_game.txt", "r")
text_value= file.read()
print(text_value)

madlib_list = {'Adjective':'',
               'Adjective':'',
               'A First Name':'',
               'Adjective':'',
               'Adjective':'',
               'Large Animal':'',
               'Small Animal':'',
               "A Girl's Name":'',
               'Adjective':'',
               }


# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
def welcome():
    user_input = input('Welcome to Madlib. Enter 3 words (2 adjectives and on noun')
    replace(text_value)


# # Replace template values
def replace(text):
    return text
    for description in madlib_list:
        print(madlib_list[description])