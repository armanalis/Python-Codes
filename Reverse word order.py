
liststring = list()

def reverse(str1):
    liststring = str1.split()
    for i in range(len(liststring)):
        newstr = liststring[i::-1]
    return newstr

str1 = input("Enter string: ")
print(reverse(str1))
