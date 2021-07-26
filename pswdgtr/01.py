import string     #string and random are two module that we are importing here.
import random

def pswdgen():
    s1=string.ascii_uppercase
    # print(s1)    #ABCDEFGHIJKLMNOPQRSTUVWXYZ

    s2=string.ascii_lowercase
    # print(s2)    #abcdefghijklmnopqrstuvwxyz

    s3=string.digits
    # print(s3)   #0123456789

    s4=string.punctuation
    # print(s4)  #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    passlen=int(input("Enter the length of password:"))

    lst=[]

    lst.extend(list(s1))   # add all characters to list
    lst.extend(list(s2))
    lst.extend(list(s3))
    lst.extend(list(s4))

    random.shuffle(lst)
    createdpass=("".join(lst[0:passlen]))
    print(createdpass)

pswdgen()
