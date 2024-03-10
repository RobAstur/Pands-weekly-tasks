#Write a program that reads in a text file and outputs the number of e's it contains.
#I suppose that the aim of this excercise is to open a file fro a folder by its name
#Author: Roberto Gomez Garcia
# Error 1: SyntaxError: Non-UTF-8 code. i was saving my file with UTF16 I found the solution in the error message see https://peps.python.org/pep-0263/ for details
# Error 2: by mistake I was trying to open the text file instead the es.py for a while. I was able to print the program but I get an sysntax error. I use debugger in this case.
# Error 3: this one was veyr complex it took me a lot of time reading forums. File "C:\Users\___\anaconda3\Lib\encodings\cp1252.py", line 23, in decode return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# To solve this issue I found the solution on https://python-forum.io/thread-6754.html. Adding enconding ="utf8" allows python to read the whole file.


f = open("mobydick.txt", "r", encoding='utf8')
test = f.read()
count = 0
for i in test:
    if "e" in i:
        count += 1
print(count)
        