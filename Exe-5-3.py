#Write a program to append all the Capital letters in a string to "caps" list and all the small letters to "small"
# named list(Input="ABcDefGHij")

input1 = "ABcDefGHij"
caps = []
small =[]
"""for i in input1:
    if i.isupper():
     #print(i)
     caps.append(i)
    else:
        i.islower()
        print("small",i)
        small.append(i)"""
def case(input1):
  for i in input1:
    if i.isupper():
        caps.append(i)
        print("caps :",i)
    else:
        small.append(i)
        print("small :",i)
def main():
    case(input1)
main()



