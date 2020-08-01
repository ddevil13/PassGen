"""MIT License Copyright (c) 2020 ddevil13

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import random
print("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n")
print("PassGen is Random Password generator created by ddevil13.\nThis software will generate a random password of size you want but does not guarantee a strong password.\nIn order to make your password a strong one give proper input and include Special characters,Uppercase letters in your passwords.\nDefault password will be a numeric password in case you want to add letters, special characters etc give proper input at each steps.\nThis software does not save any password for security reasons in case you want to save it copy and save it in your safe custody.\nIn case you find an issue or for suggestions feel free to raise it on GitHub at this link: https://github.com/ddevil13/PassGen/")

def getint(name,msg):
    while True:
        try:
            name=int(input(f"{msg}\n"))
        except ValueError:
            print("Only numbers are allowed\n")
            getint(name,msg)
        if name>=0:
            break
        else:
            print("Only Positive number is allowed\n")
    ret=name
    return ret    
def getbool(name,msg):
    while True:
        try:
            name=int(input(f"{msg}\n"))
        except ValueError:
            print("Only numbers are allowed\n")
            getbool(name,msg)
        if name==0 or name==1:
            break
        else:
            print("Only 1 or 0 is allowed\n")
    ret=bool(name)
    return ret

pwdlen=0
wordlen=0
upperwordlen=0
specialcharlen=0
numericlen=0
wordsflag=0
specialcharflag=0

pwdlen=getint(pwdlen,"What length password you want to generate: ")
wordsflag=getbool(wordsflag,"Do you want to add letters to your password(1(Yes),0(No))")
if wordsflag==True:
    wordlen=getint(wordlen,f"How much number of letters out of {pwdlen} you want?: ")
    while True:
        if wordlen>pwdlen:
            print("Number of letters are more than password length! Give proper number: \n")
            wordlen=getint(wordlen,f"How much number of letters out of {pwdlen} you want?: ")
        else:
            upperwordlen=getint(upperwordlen,"How much letters from above should be in UPPERCASE?: ")
            while True:
                if upperwordlen>wordlen:
                    print("Number of UpperLetter are more than letter length! Give proper number: \n")
                    upperwordlen=getint(upperwordlen,"How much letters from above should be in UPPERCASE?: ")
                else:
                    break
            break
else:
    wordlen=0
    upperwordlen=0
specialcharflag=getbool(specialcharflag,"Do you want to add any special character(1(Yes),0(No))")
if specialcharflag==True:
    specialcharlen=getint(specialcharlen,f"How much number of Special Character out of {pwdlen} you want?: ")
    while True:
        if specialcharlen>pwdlen:
            print("Number of Special Character are more than password length! Give proper number: \n")
            specialcharlen=getint(specialcharlen,f"How much number of Special Character out of {pwdlen} you want?: ")
        elif pwdlen<wordlen+specialcharlen:
            print("Number of Special Character and Letters are more than password length! Give proper number: \n")
            specialcharlen=getint(specialcharlen,f"How much number of Special Character out of {pwdlen} you want?: ")
        else:
            break
else:
    specialcharlen=0

numericlen=pwdlen-specialcharlen-wordlen
wordlen=wordlen-upperwordlen

specialchar=""
numeric=""
word=""
upperword=""

while specialcharlen>0:
    s=random.choice("@%\/+!#₹^?':,(){}[]~-_.")
    specialchar=specialchar+s
    specialcharlen-=1
    
while numericlen>0:
    n=random.choice('1234567890')
    numeric=numeric+n
    numericlen-=1
    
while wordlen>0:
    w=random.choice('abcdefghijklmnopqrstuvwxyz')
    word=word+w
    wordlen-=1
    
while upperwordlen>0:
    u=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    upperword=upperword+u
    upperwordlen-=1

pwd=specialchar+upperword+word+numeric
pwdl=list(pwd)
random.shuffle(pwdl)
pwd="".join(pwdl)

print(f"Here is your password: {pwd}")
print("Thank you for using PassGen.\nCreated by ddevil13.")