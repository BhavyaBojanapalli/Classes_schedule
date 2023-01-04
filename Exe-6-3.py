#Write a program to print the below output
#languages = ['Swift', 'Python', 'Go', 'JavaScript']
#output:
#Swift
#My fav programming language
#Go
#JavaScript

#for and if
def test(languages):
    l_replace = ['My fav programming language' if 'Python' in i else i for i in languages]
    print(l_replace)
def main():
    languages = ['Swift', 'Python', 'Go', 'JavaScript']
    test(languages)
main()

"""
def test(languages):
    for i in languages:
        print(i)
def main():
    languages = ['Swift', 'Python', 'Go', 'JavaScript']
    test(languages)
main()"""
