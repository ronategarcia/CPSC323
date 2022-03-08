#Name: Rodrigo Onate
#Date: March 01, 2022
#Class: CPSC323 - 03
#Description: Project 1

"""Main module for removing comment lines that start with //
    and adding spaces before and after each token
"""


def white_space(line):
    """Method to delete all white space"""
    white_space = " "
    i = 0
    while i < len(line):
        if line[i] == white_space:
            line = line[:i] + line[i+1:]
        else:
            i += 1
    return line


def begin_with(line):
    """Method that checks if there is '//' at the beginning of string"""
    if line[0] == '/' and line[1] == '/':
        return True
    return False


def rep_str(line):
    """Method that adds spaces before and after token"""
    if 'cout<<' in line:           
        line = line.replace('cout<<', 'cout<< ')   
    if '=' in line:
        line = line.replace('=', ' = ')   
    if '+' in line:
        line = line.replace('+', ' + ')
    if 'int' in line:
        line = line.replace('int', 'int ')
    if ',' in line:
        line = line.replace(',', ' , ')
    if ';' in line:
        line = line.replace(';', ' ; ')
    return line


with open('data.txt', 'r') as read_file:
    with open('newdata.txt', 'w') as write_file:
        for line in read_file:
            line = white_space(line)
            if not begin_with(line):
                line = rep_str(line)
                write_file.write(line)
