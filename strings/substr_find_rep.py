# Author: Pranav Shridhar
# Python 3
# Replaces a substring with a different string.  India - > (ia) replace with (onasia) -> Indonasia 

def myFind(str, substr, repstr):
    for i in range(len(str)):
        if str[i:i+len(substr)] == substr:
            str = str[:i]+repstr+str[i+len(substr):] 
    if substr not in str:
        print(str)
    else:
        myFind(str, substr, repstr)

string = input('Enter a sentence : ')
substring = input('Enter substring to find and replace : ')
r_substring = input('Enter a substring to replace it with : ')
myFind(string, substring, r_substring)
