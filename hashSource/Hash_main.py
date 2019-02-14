#All rights reserved accordingly. Contact author at edward.anguiano@edwardssite.com for more information.
#Why make code understandable when if it is not, it's completely your own? 
#Because if it is understandable, it is no longer your own.

#imports important systems.
import sys
import os
import os.path
import Clear_Screen
import Hash_MD5
import Hash_SHA1

#Creates arguments that represent other arguments
_cls = Clear_Screen.cls
_m5f = Hash_MD5.f
_m5s = Hash_MD5.s
_s11f = Hash_SHA1.f
_s11s = Hash_SHA1.s

_cls()
print("Hash program")
print("for more options, type Help")
while True:
    _input1 = input('[S]tring or [F]ile: ')
    _i1 = _input1.lower().strip().replace(' ','')
    if _i1 == 'file' or _i1 == 'f':
        filePath = input('File Path: ')

        if os.path.exists(filePath):
            _hash = input('Hash Method: ')
            _h = _hash.lower().strip().replace(' ','')
            
            if _h == 'md5':
                _m5f(filePath)
                _nul = input('Press Enter to continue...')
                _cls()

            elif _h == 'sha1':
                _s11f(filePath)
                _nul = input('Press Enter to continue...')
                _cls()
        else:
            print("File Not found.")
    elif _i1 == 'string' or 's':
        _str = input('String: ')
        
        _in2 = input('Strip whitespace? ([Y]es | [N]o)')
        _i2 = _in2.strip().lower().replace(' ','')
        
        _hash = input('Hash method: ')
        _h = _hash.strip().lower().replace(' ','')
       
        print('')

        if (_i2 == 'yes' or _i2 == 'y') and (_h == 'md5'):
            _sstr = _str.strip()
        
            print('String: ' +  _sstr)
            _m5s(_sstr)
            _nul = input('Press Enter to continue...')
            _cls()

        if (_i2 == 'yes' or _i2 == 'y') and (_h == 'sha1'):
            _sstr = _str.strip()
        
            print('String: ' +  _sstr)
            _s11s(_sstr)
            _nul = input('Press Enter to continue...')
            _cls()
        
        elif (_i2 == 'no' or _i2 == 'n') and (_h == 'md5'):
            print('String: ' + _str)
            _m5s(_str)
            _nul = input('Press Enter to continue...')
            _cls()

        elif (_i2 == 'no' or _i2 == 'n') and (_h == 'sha1'):
            print('String: ' + _str)
            _s11s(_str)
            _nul = input('Press Enter to continue...')
            _cls()




            