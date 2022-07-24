import re

# Set default template
madlib_result= ""
madlib_words=[]
madlib_template=""

def read_template(filepath="dark_and_stormy_night.txt"):
    try:
        file = open(filepath, "r")

        madlib_template = file.read().strip()
        file.close()
        parse_template(madlib_template)

    except FileNotFoundError as fe:
        #Notify user of error
        print(f'Sorry. {fe.strerror}')




def parse_template(madlib_template):
    regex = r"{(.*?)}"
    words = []
    try:

    #Original reference
        regex = r'(w+)s*[^{]*{s*([^}]+)s*}'
            # printing original string https://www.geeksforgeeks.org/python-extract-substrings-between-brackets/
        print("The original string is : " + madlib_template)

            # Extract substrings between brackets
            # Using regex
        words = re.findall(r'\{.*?\}', madlib_template)


            # printing result
       # print("The element between brackets : " + str(words))



    except TypeError:
        print(TypeError.__str__())
    #return string and tuple
    #
    finally:

        merge(words,madlib_template)
def merge(words,template):
    # Loop through extracted words and prompt user for input
    for x in words:
        user_input = input(f'Enter a/an {x}:')
        madlib_words.append(user_input)
        print(f'{x}: {user_input}')

        #Save the user's imput
        filedata = template.replace(x, user_input,1)
        template = filedata

    # Write to new file   template = filedata
    f = open("dark_and_stormy_night_output.txt", "w")
    f.write(filedata)
    f.close()

    print(filedata)

read_template()
