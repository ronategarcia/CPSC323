#Name: Rodrigo Onate
#Date: March 01, 2022
#Class: CPSC323 - 03
#Description: Project 1

"""Main module to read a string from user and identify each token """

res_words = ['cout<<', 'for', 'int', 'while']
s_token = ['<', '=', '*', '-', ';', '(', ')', '<=', '+', ',']
count = 0
x = 0
state = True
while state:
    i_string = input("Enter a statement: ")
    if len(i_string) > 255:
        print("String longer than 255 characters")
    else:
        while count < len(i_string):
            sub_string = ' '
            if i_string[count] == ' ':
                sub_string = i_string.split(' ')[x]
                up_substring = ''
                if sub_string[0].isupper():
                    up_substring = sub_string[0].lower()+sub_string[1:]
                    if up_substring in res_words:
                        print(sub_string, end=' ')
                        print('reserved word')
                    elif sub_string.isalpha() not in res_words:
                        print(sub_string, end=' ')
                        print('identifier')
                    x+=1
                else:
                    if sub_string in res_words:
                        print(sub_string, end=' ')
                        print('reserved word')
                    elif sub_string in s_token:
                        print(sub_string, end=' ')
                        print('special symbol')
                    elif sub_string.isdigit():
                        print(sub_string, end=' ')
                        print('number')
                    elif sub_string[0] == '-' and sub_string[1].isdigit():
                        print(sub_string, end=' ')
                        print('number')
                    elif sub_string.isalpha() or sub_string[0] == '_':
                        print(sub_string, end=' ')
                        print('identifier')
                    else:
                        print(sub_string, end=' ')
                        print('not identifier')
                    x+=1
            count+=1
            if count == len(i_string)-1:
                if i_string[count] == ';':
                    print('; special symbol')    
                else:
                    print("Missing special symbol ';' and previous character")
        n = input("CONTINUE(y/n)?")
        if n == 'y' or n == 'Y':
            count = 0
            x = 0
            state = True
        elif n == 'n' or n == 'N':
            state = False
