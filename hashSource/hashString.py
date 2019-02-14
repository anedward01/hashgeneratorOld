#imports modules from system and subdirectories
import sys
import os
import os.path
import subFiles.cls
import hashFiles.md5
import hashFiles.sha1
import hashFiles.sha224
import hashFiles.sha256
import hashFiles.sha384
import hashFiles.sha512
import hashFiles.sha3_224
import hashFiles.sha3_256
import hashFiles.sha3_384
import hashFiles.sha3_512
import hashFiles.shake128
import hashFiles.shake256

#Defines arguments used later in the code.
_cls____ = subFiles.cls.cls
_m5s____ = hashFiles.md5.s
_s1_1s = hashFiles.sha1.s
_s1_224s = hashFiles.sha224.s
_s1_256s = hashFiles.sha256.s
_s1_384s = hashFiles.sha384.s
_s1_512s = hashFiles.sha512.s
_s3_224s = hashFiles.sha3_224.s
_s3_256s = hashFiles.sha3_256.s
_s3_384s = hashFiles.sha3_384.s
_s3_512s = hashFiles.sha3_512.s
_sh_128s = hashFiles.shake128.s
_sh_256s = hashFiles.shake256.s

def s(n):
    for i in range(999999):
        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        print('File Path: "' + n + '"')

        if hType == 'md5':
            _m5s____(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha1':
            _s1_1s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha224':
            _s1_224s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha256':
            _s1_256s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n
        
        elif hType == 'sha384':
            _s1_384s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha512':
            _s1_512s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3224':
            _s3_224s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3256':
            _s3_256s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3384':
            _s3_384s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3512':
            _s3_512s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'shake128':
            _sh_128s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3512':
            _sh_256s(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

    else:
        print("Hash not found!")