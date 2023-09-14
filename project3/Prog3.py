# Rodrigo Onate 
# 2022/05/02
# CPSC323
# Project 3 - program 3



def list_to_str(alist):
    str_ing = ''
    for x in alist:
        str_ing += x
    return str_ing

str_list = []
stack_list = ['0']
a_dict = {
    '0': {'i': ['S', '5'], '(': ['S', '4'], 'E': '1', 'T': '2', 'F': '3'},
    '1': {'+': ['S', '6'], '-': ['S', '7'], '$': 'ACC'},
    '2': {'+': ['R', '3'], '-': ['R', '3'], '*': ['S', '8'], '/': ['S', '9'], ')': ['R', '3'], '$': ['R', '3']},
    '3': {'+': ['R', '6'], '-': ['R', '6'], '*': ['R', '6'], '/': ['R', '6'], ')': ['R', '6'], '$': ['R', '6']},
    '4': {'i': ['S', '5'], '(': ['S', '4'], 'E': '10', 'T': '2', 'F': '3'},
    '5': {'+': ['R', '8'], '-': ['R', '8'], '*': ['R', '8'], '/': ['R', '8'], ')': ['R', '8'], '$': ['R', '8']},
    '6': {'i': ['S', '5'], '(': ['S', '4'], 'T': '11', 'F': '3'},
    '7': {'i': ['S', '5'], '(': ['S', '4'], 'T': '12', 'F': '3'},
    '8': {'i': ['S', '5'], '(': ['S', '4'], 'F': '13'},
    '9': {'i': ['S', '5'], '(': ['S', '4'], 'F': '14'},
    '10': {'+': ['S', '6'], '-': ['S', '7'], ')': ['S', '15']},
    '11': {'+': ['R', '1'], '-': ['R', '1'], '*': ['S', '8'], '/': ['S', '9'], ')': ['R', '1'], '$': ['R', '1']},
    '12': {'+': ['R', '2'], '-': ['R', '2'], '*': ['S', '8'], '/': ['S', '8'], ')': ['R', '2'], '$': ['R', '2']},
    '13': {'+': ['R', '4'], '-': ['R', '4'], '*': ['R', '4'], '/': ['R', '4'], ')': ['R', '4'], '$': ['R', '4']},
    '14': {'+': ['R', '5'], '-': ['R', '5'], '*': ['R', '5'], '/': ['R', '5'], ')': ['R', '5'], '$': ['R', '5']},
    '15': {'+': ['R', '7'], '-': ['R', '7'], '*': ['R', '7'], '/': ['R', '7'], ')': ['R', '7'], '$': ['R', '7']}
}

in_string = input('Enter a string: ')
in_string = in_string.replace(" ", "")
str_list[:0] = in_string
print('\n')
print(f"{'Stack':30}{'Input String':20}{'Table entry':20}")
print(f"{'=====':30}{'============':20}{'===========':20}")

while str_list[0] != '$':
    if stack_list[-1] in a_dict.keys() and str_list[0] in a_dict[stack_list[-1]].keys():
        val = a_dict[stack_list[-1]].get(str_list[0])

        if val[0] == 'S':
            print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
            stack_list.append(str_list[0])
            stack_list.append(val[1])
            del str_list[0]
        elif val[0] == 'R':         
            if val[1] == '1':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'E':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '2':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'E':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '3':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('E')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '4':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '5':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '6':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'F':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('T')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '7':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != '(':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('F')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '8':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'i':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('F')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)

val = a_dict[stack_list[-1]].get(str_list[0])
while val != 'ACC':
    if stack_list[-1] in a_dict.keys() and str_list[0] in a_dict[stack_list[-1]].keys():
        val = a_dict[stack_list[-1]].get(str_list[0])

        if val[0] == 'S':
            print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
            stack_list.append(str_list[0])
            stack_list.append(val[1])
            del str_list[0]
        elif val[0] == 'R':         
            if val[1] == '1':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'E':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '2':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'E':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '3':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('E')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '4':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '5':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'T':
                    stack_list.pop()
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '6':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'F':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('T')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '7':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != '(':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('F')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
            elif val[1] == '8':
                print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1]):19}')
                while stack_list[-1] != 'i':
                    stack_list.pop()
                stack_list.pop()
                stack_list.append('F')
                y = a_dict[stack_list[-2]].get(stack_list[-1])
                stack_list.append(y)
print(f'{list_to_str(stack_list):30}{list_to_str(str_list):20}{list_to_str(val[0])}{list_to_str(val[1])}{list_to_str(val[2]):18}')
