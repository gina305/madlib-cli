# Read the file and save it to a variable
user_results =[]

def readFile():
    file = open("make_me_a_video_game.txt", "rb")
    text_value = file.read()
    print(text_value)
    mad_array = []
    # Define
    txt = text_value.split()

    madlib_list = {'Adjective1': '',
                   'Adjective2': '',
                   'A First Name': '',
                   'Adjective3': '',
                   'Adjective4': '',
                   'Large Animal': '',
                   'Small Animal': '',
                   "A Girl's Name": '',
                   'Adjective5': ''
                   }

    for line in madlib_list:
        ask(line)







# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
def welcome(text_value,madlib_list):
    user_input = input(f'Welcome to Madlib. Enter {len(madlib_list)} words:')
    replace(text_value)
    # for q in madlib_list:
    #     selection = input(f'+ Choose a {q}: ')
    #


# # Replace template values
def replace(new_text, old_text):
    return text
    #for description in madlib_list:
# print(madlib_list)

def ask(q):
    user_input=input(f'* Select a/an {q} ')
    user_results.append(user_input)
    print(user_results.index())
    replace(q, user_input)

readFile()