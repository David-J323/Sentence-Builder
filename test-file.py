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
        self.inputArr = [self.userNoun] + [self.userAdjective] + [self.userSubject]
        self.sentenceArr = []
        self.paragraphArr = []
        self.newSentence = ''
        self.newParagraph = ''
        self.sentencePart1 = ''
        self.sentencePart2 = ''
        self.sentencePart3 = ''
        self.space = ' '
        self.counter = 1
        self.digits = string.digits
        self.alphabet = string.ascii_letters
    

    def random(self):
        multiArr = [['That', 'is a very', '. ' ], ['The', 'can be such a fucking', '. '], ['Fuck', 'cuz that', ' can eat my ass. '], ['You are such a', 'stupid', '. '], ['Why', 'can\'t you be a', '. ']]
        #for y in multiArr:
         #   print(y)
        randomGenerator = secrets.choice(multiArr)
        self.sentenceArr = randomGenerator
        #print(self.sentenceArr)
        self.builder()

    def builder(self):
        #randomize input array
        #print(self.inputArr)
        randomArr = []
        for z in self.inputArr:
            z = secrets.choice(self.inputArr)
            randomArr = randomArr + [z]
        print(randomArr)
        self.newSentence = self.sentenceArr[0] + ' ' + self.sentencePart1 + ' ' + self.sentenceArr[1] + ' ' + self.sentencePart2 + ' ' + self.sentencePart3 + self.sentenceArr[2] 
        #print(self.newSentence)        
        self.paragraphs()
        #goal - put same inputs in different places

    def paragraphs(self):
        self.paragraphArr = self.paragraphArr + [self.newSentence]
        self.newParagraph = self.newParagraph + self.newSentence
        #for w in self.paragraphArr:
            #self.newParagraph = w
        if(self.counter < 5):
            self.counter = self.counter + 1
            self.random()
        else:
            print(self.paragraphArr)
            print(self.newParagraph)
            print('stop')
            return


noun = input("Which noun do you want to use? ")
subject = input ('What subject do you want to use? ')
adjective = input('What adjective do you want to use? ')
x = sentenceBuilder(noun, subject, adjective)
x.random()


#multiArr = [['That ', 'is a very ', '.' ], ['The ', 'can be such a fucking ', '.'], ['Fuck ', 'cuz that ', 'can eat my ass.']]
#print(multiArr[0][0] + multiArr[1][1] + multiArr[2][0])


#for machine learning 4 lists may be needed
#1 for the actual array of possible sentences
#2 for the record of sentences built with user input
#3 for the record of paragraphs built with constructed sentences
#4 for the record of user inputs made