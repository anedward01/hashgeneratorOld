#Created by Anguianoewi. 2019-02-14

#imports modules
import sys
import os
import subFiles.cls
import subFiles.title

#Defines arguments used in the code
_cls____ = subFiles.cls.cls
_version = subFiles.title.version

#Endless loop until exit
def h():
    _cls____()
    print('Hash Converter Help.')
    while True:
        print('[H]ash Methods | [C]redits | [E]xit')
        helpOption = input()
        hOpt = helpOption.lower().strip().replace(' ','')
        if hOpt == 'hashmethods' or hOpt == 'h' or hOpt == 'hash' or hOpt == 'hashmethod':
            print('''The following hash methods are available:
    MD5     | SHA 384   | SHA3 384
    SHA 1   | SHA 512   | SHA3 512
    SHA 224 | SHA3 224  | SHAKE 128 (64 bit)
    SHA 256 | SHA3 256  | SHAKE 256 (64 bit)''')
            print('')
            cont = input()
            _cls____()
            True
        elif hOpt == 'c' or hOpt == 'credits' or hOpt == 'credit':
            print('Hash Generator Version ' + _version())
            print('For suggestions, visit https://github.com/anguianoewi/hashgenerator')
            print('This code is free to use. Only requirement is to give credit where due')
            print('Author: Anguianoewi')
            print('')
            print('I wrote this code like, eight months ago into one large file')
            print('and broke it down in three days, so I need to find my list of')
            print('contributors because they deserve credit too.')
            cont = input()
            _cls____()
            True
        elif hOpt == 'e' or hOpt == 'exit':
            _cls____()
            return hOpt
        else:
            False
            
