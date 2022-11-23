class wordCounter:
    def __init__(self, stringWord):
        self.stringWord=stringWord
    def dictionCreator(self):
        diction={}
        for letter in self.stringWord:
            if letter.isalpha():
                diction[letter]=diction.get(letter,0)+1
        return diction
    def __str__(self):
        return "For the string, \"" + self.stringWord + "\" here is the dictionary values:" + str(self.dictionCreator())
    def printing(self):
        print("For the string, \"" + self.stringWord + "\" here is the dictionary values: " )
        diction = self.dictionCreator()
        for letter in diction:
            print(f"{letter}: {diction[letter]}")

class listCombine:
    list3=[]
    def __init__(self, list1, list2):
        self.list1=list1
        self.list2=list2
    def combine(self):
        listCombine.list3.extend(self.list1)
        listCombine.list3.extend(self.list2)
        return str(listCombine.list3)
    def __str__(self):
        return self.combine()

    
class fileShiz:
    def __init__(self, file, text):
        self.file=file
        self.text= text
        self.val= listCombine([1,2,3],[4,5,6]).combine()
    def changeText(self,text):
        self.text=text
    def openAndWrite(self):
        with open ("files/"+self.file,"w") as fileOpener:
            fileOpener.write(self.text +"\n")
    def openAndAppend(self):
        with open ("files/"+self.file,"a") as fileOpener:
            fileOpener.write(self.text +"\n")

class fileShizInherit(listCombine):
    def __init__(self, file, text, list1, list2):
        self.file=file
        self.text= text
        self.list1 = super().__init__(list1,list2)
    def changeText(self,text):
        self.text=text
    def openAndWrite(self):
        with open ("files/"+self.file,"w") as fileOpener:
            fileOpener.write(self.text +"\n")
    def openAndAppend(self):
        with open ("files/"+self.file,"a") as fileOpener:
            fileOpener.write(self.text +"\n")
        
        


def main():
    firstObj= wordCounter("I like how the Nichijou OPs basically summarize and spoil what the anime is about but at the same time, it doesn't.")
    firstObj.printing()
    print(str(firstObj) +"\n")
    firstList= listCombine([1,2,3], [4,5,6])
    secondList= listCombine([1,2,3], [4,5,6])
    print(firstList)
    print(secondList)
    firstFile= fileShiz("create.txt", "Write this to the file")
    firstFile.openAndWrite()
    firstFile.changeText("This is the new text")
    firstFile.openAndAppend()
    firstFile.openAndWrite()

main()