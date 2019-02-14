#Created by Anguianoewi. 2019-02-13

#imports modules from system and subdirectories
import sys
import os
import os.path
import hashFile
import hashString
import subFiles.cls
import subFiles.title
import helpMain

#Defines arguments used later in the code.
_cls____ = subFiles.cls.cls         #Clear command prompt or terminal code
_title__ = subFiles.title.title     #Title command prompt only
_help___ = helpMain.h               #Help file argument
_version = subFiles.title.version   #Identifies program version

#cleans screen before starting
_cls____()

#titles program if in command prompt
_title__()

#Endless loop until end
while True:

    #Titles program
    print("Hash converter Version " + _version())

    #asks for file or string
    fileType = input('[S]tring | [F]ile | [H]elp | [E]xit: ')
    fType = fileType.lower().replace(' ','').strip()

    #identifies if input requests a file hash
    if fType == 'file' or fType == 'f':

        #asks for file path
        filePath = input('File Path: ')

        #identifies if file path exists
        if os.path.exists(filePath):

            #Runs File Hash program
            hashFile.f(filePath)
            
    #identifies if input request a string text hash
    elif fType == 'string' or fType == 's':
        string = input('String: ')

        #asks if the program should remove trailing spaces
        #For example, "Hello  " to "Hello"
        stringStrip = input('Strip white space? ([Y]es | [N]o)')
        sStrip = stringStrip.lower().strip().replace(' ','')

        #Strips trailing whitespace
        if sStrip == 'yes' or sStrip == 'y':
            sString = string.strip()
            hashString.s(sString)
            
        #Keeps string intact    
        if sStrip == 'no' or sStrip == 'n':
            hashString.s(string)
            
    #identifies if the input requests help
    elif fType == 'h' or fType == 'help':
        _help___()
        
    #identifies if the input request to quit     
    elif fType == 'e' or fType == 'exit':
        sys.exit()
