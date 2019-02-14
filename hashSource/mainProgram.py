#Created by Anguianoewi. 2019-02-13

#imports modules from system and subdirectories
import sys
import os
import os.path
import hashFile
import hashString
import subFiles.cls

#Defines arguments used later in the code.
_cls____ = subFiles.cls.cls

#cleans screen before starting
_cls____()

#Title of program
print("Hash converter Version 1.0")
print('For more options, type [H]elp')

#Endless loop until end
while True:
    
    #asks for file or string
    fileType = input('[S]tring or [F]ile: ')
    fType = fileType.lower().replace(' ','').strip()

    if fType == 'file' or fType == 'f':
        filePath = input('File Path: ')
        if os.path.exists(filePath):
            hashFile.f(filePath)
    
    elif fType == 'string' or fType == 's':
        string = input('String: ')
        stringStrip = input('Strip white space? ([Y]es | [N]o)')
        sStrip = stringStrip.lower().strip().replace(' ','')
        if sStrip == 'yes' or sStrip == 'y':
            sString = string.strip()
            hashString.s(sString)
        if sStrip == 'no' or sStrip == 'n':
            hashString.s(string)

        