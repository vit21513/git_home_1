#test func for git

from random import randint


def remake(stroka: str):
    """random creaty text"""
    temp =str()
    for i in range(len(stroka)):
        temp+=stroka[randint(0,len(stroka))-1]
    return temp    
       

if __name__== "__main__":
    print(remake("i want to tell about picture"))        