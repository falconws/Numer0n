#!/usr/bin/env python
#*-* coding:utf-8 -*-

import random

class Numeron:

    keta = 0
    answer = []
    userInput = []
    log = []
    eat = 0
    bite = 0

    def __init__(self, keta):
        self.keta = keta
        self.eat = 0
        self.bite = 0

        i = 0
        while i < self.keta:
            randomNumber = random.randint(0, 9)
            if randomNumber in self.answer:
                i -= 1
            else:
                self.answer.append(randomNumber)

            i += 1

        # debug
        # print self.answer

    def _checkEAT(self, input):
        for i in xrange(self.keta):
            if self.answer[i] == input[i]:
                self.eat += 1

    def _checkBITE(self, input):
        for i in input:
            if i in self.answer:
                self.bite += 1

        self.bite -= self.eat

    def _writeLog(self):
        uInput = ""
        for i in self.userInput:
            uInput += str(i)

        self.log.append(uInput + " : " + str(self.eat) + 
                        "EAT " + str(self.bite) + "BITE")

    def _showLog(self):
        print "\n".join(self.log)

    def _strToList(self, uInput):
        for i in xrange(self.keta):
            self.userInput.append(int(uInput[i]))

    def _isValid(self, uInput):
        if len(uInput) != self.keta:
            return False

        if not uInput.isdigit():
            return False

        return True
    
    def challenge(self):
        while True:
            uInput = raw_input(str(self.keta) + '桁の数値を入力して下さい\n')
            # command
            if uInput == "giveup":
                break

            if not self._isValid(uInput):
                continue

            self._strToList(uInput)
            self._checkEAT(self.userInput)
            self._checkBITE(self.userInput)

            if self.eat == self.keta:
                print "正解です。\n"
                break

            self._writeLog()
            self._showLog()

            self.eat = 0
            self.bite = 0
            self.userInput = []

        print "答え = " + str(self.answer)        


if __name__ == '__main__':
    KETA = 3
    numeron = Numeron(KETA)
    numeron.challenge()
