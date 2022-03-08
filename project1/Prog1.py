#Name: Rodrigo Onate
#Date: March 01, 2022
#Class: CPSC323 - 03
#Description: Project 1

"""Main module for L = (a|b)*bb*a"""
table_list = ((0,1),(2,1),(0,1))
r = 0
status = True

while status:
    USR_IN = input("Enter string with only a's and b's and a $ at the end: ")
    for i in USR_IN:
        if i == 'a':
            r = table_list[r][0]
        elif i == 'b':
            r = table_list[r][1]
        elif i == '$':
            if r == 2:
                print("YES")
            else:
                print("NO")
    answer = input("Do you want to enter another string? (Y/n)")
    if answer in ('Y', 'y'):
        status = True
    elif answer in ('N', 'n'):
        status = False
