import os
import string
import secrets
from typing import final 

class sentenceBuilder: 
    def __init__(self, userNoun, userSubject, userAdjective): 
        self.word = ''
        self.letter = ''
        self.userNoun = userNoun
        self.userSubject = userSubject
        self.userAdjective = userAdjective
        self.sentenceArr = []
        self.paragraphArr = []
        self.newSentence = ''
        self.space = ' '
        self.digits = string.digits
        self.alphabet = string.ascii_letters
    

    def random(self):
        multiArr = [['That', 'is a very', '.' ], ['The', 'can be such a fucking', '.'], ['Fuck', 'cuz that', 'can eat my ass.']]
        #for y in multiArr:
         #   print(y)
        randomGenerator = secrets.choice(multiArr)
        self.sentenceArr = randomGenerator
        print(self.sentenceArr)
        self.builder()

    def builder(self):
        self.newSentence = self.sentenceArr[0] + ' ' + self.userSubject + ' ' + self.sentenceArr[1] + ' ' + self.userAdjective + ' ' + self.userNoun + self.sentenceArr[2] 
        print(self.newSentence)        
        self.paragraphs()

    def paragraphs(self):
        self.paragraphArr = self.paragraphArr + [self.newSentence]
        print(self.paragraphArr)
        for z in self.paragraphArr:
            if(z < 5):
                self.random()
            else:
                print('stop')
                return


noun = input("Which noun do you want to use? ")
subject = input ('What subject do you want to use? ')
adjective = input('What adjective do you want to use? ')
x = sentenceBuilder(noun, subject, adjective)
x.random()


#multiArr = [['That ', 'is a very ', '.' ], ['The ', 'can be such a fucking ', '.'], ['Fuck ', 'cuz that ', 'can eat my ass.']]
#print(multiArr[0][0] + multiArr[1][1] + multiArr[2][0])