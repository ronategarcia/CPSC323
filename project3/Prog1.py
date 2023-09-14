# Rodrigo Onate
# CPSC323
# Project 2 - Question 7
# 2022/04/06

"""Program to trace and imput string given by the user"""


def list_to_str(alist):
    str_ing = ''
    for x in alist:
        str_ing += x
    return str_ing

str_list = []
stack_list = ['$', 'S']
symbols = ['a', '+', '-', '*', '/', '(', ')', '$', 'b', '=']
states = ['E', 'Q', 'T', 'R', 'F', 'S']
valid = [('Q', 'T'), ('Q', 'T', '+'), ('Q', 'T', '-'), ('R', 'F'), ('R', 'F', '*'), ('R', 'F', '/'), 'a', (')', 'E', '('), ('E', '=', 'a'), 'b']
##            0              1                2            3               4               5           6           7              8          9
in_string = input('Enter a string: ')
in_string = in_string.replace(" ", "")
print('\n')
print(f"{'Stack':20}{'Input String':10}")
print(f"{'=====':20}{'============':10}")
str_list[:0] = in_string
while str_list[0] != '$':
    if str_list[0] == 'a' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == 'a' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == 'a' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[6])
    elif str_list[0] == 'a' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == 'a' and stack_list[-1] == states[5]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[8][0])
        stack_list.append(valid[8][1])
        stack_list.append(valid[8][2])
    elif str_list[0] == 'b' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == 'b' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == 'b' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[9])
    elif str_list[0] == 'b' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '=' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '+' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[1][0])
        stack_list.append(valid[1][1])
        stack_list.append(valid[1][2])
    elif str_list[0] == '+' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '+' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '-' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[2][0])
        stack_list.append(valid[2][1])
        stack_list.append(valid[2][2])
    elif str_list[0] == '-' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '-' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '*' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[4][0])
        stack_list.append(valid[4][1])
        stack_list.append(valid[4][2])
    elif str_list[0] == '*' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '/' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[5][0])
        stack_list.append(valid[5][1])
        stack_list.append(valid[5][2])
    elif str_list[0] == '/' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '(' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == '(' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == '(' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[7][0])
        stack_list.append(valid[7][1])
        stack_list.append(valid[7][2])
    elif str_list[0] == '(' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == ')' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == ')' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == ')' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del str_list[0]
    else:
        break

while stack_list[-1] != '$':
    if str_list[0] == 'a' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == 'a' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == 'a' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[6])
    elif str_list[0] == 'a' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == 'a' and stack_list[-1] == states[5]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[8][0])
        stack_list.append(valid[8][1])
        stack_list.append(valid[8][2])
    elif str_list[0] == 'b' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == 'b' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == 'b' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[9])
    elif str_list[0] == 'b' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '=' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '+' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[1][0])
        stack_list.append(valid[1][1])
        stack_list.append(valid[1][2])
    elif str_list[0] == '+' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '+' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '-' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[2][0])
        stack_list.append(valid[2][1])
        stack_list.append(valid[2][2])
    elif str_list[0] == '-' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '-' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '*' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[4][0])
        stack_list.append(valid[4][1])
        stack_list.append(valid[4][2])
    elif str_list[0] == '*' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '/' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[5][0])
        stack_list.append(valid[5][1])
        stack_list.append(valid[5][2])
    elif str_list[0] == '/' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == '(' and stack_list[-1] == states[0]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[0][0])
        stack_list.append(valid[0][1])
    elif str_list[0] == '(' and stack_list[-1] == states[2]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[3][0])
        stack_list.append(valid[3][1])
    elif str_list[0] == '(' and stack_list[-1] == states[4]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        stack_list.append(valid[7][0])
        stack_list.append(valid[7][1])
        stack_list.append(valid[7][2])
    elif str_list[0] == '(' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == ')' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
        del str_list[0]
    elif str_list[0] == ')' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == ')' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] == states[1]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] == states[3]:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del stack_list[-1]
    elif str_list[0] == '$' and stack_list[-1] in symbols:
        print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
        del str_list[0]
    else:
        break
print(f'{list_to_str(stack_list):20}{list_to_str(str_list):10}')
if str_list[0] == '$' and stack_list[-1] == '$':
    print('Accepted')
else:
    print('Not accepted')