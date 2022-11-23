import random

class numGuess:
    def __init__(self):
        self.randNum= random.randint(1,10)
    def getNum(self):
        return self.randNum
    def guess(self):
        value= input("Choose a number (1-10)")
        return value



def main():
    randomg= numGuess()
    rand= randomg.getNum()
    val= randomg.guess()
    while val != randomg.getNum():
        val= randomg.guess()
    print("Congrats! You got the number correct which was" + randomg.getNum())


main()


    