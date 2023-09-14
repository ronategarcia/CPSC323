# Rodrigo Onate 
# 2022/05/02
# CPSC323
# Project 3 - program 2

stack_list = []
str_list = []
letters = {}
status = True

while status:
    str_inp = input('Enter a postfix expression with a $ at the end: ')
    for i in str_inp:
        if i.isalpha() and i not in letters:
            letters[i] = ''
    for i in letters:
        in_put = input('\tEnter the value of ' + i + ': ')
        letters[i] = in_put
    for i in str_inp:
        if i.isalpha():
            if i in letters.keys():
                str_list.append(letters.get(i))
        else:
            str_list.append(i)
    str_list.pop()
    for i in str_list:
        if i.isdigit():
            i = int(i)
            stack_list.append(i)
        else:
            f_num = stack_list.pop()
            s_num = stack_list.pop()

            if i == '+':
                stack_list.append(s_num + f_num)
            elif i == '-':
                stack_list.append(s_num - f_num)
            elif i == '*':
                stack_list.append(s_num * f_num)
            elif i == '/':
                stack_list.append(s_num // f_num)
    print('\t\tFinal value= ', end='') 
    print(stack_list.pop())

    cont = input('Continue(y/n)?')
    if cont in ('n', 'N'):
        status = False
    elif cont in ('y', 'Y'):
        stack_list = []
        letters = {}
        str_list = []
