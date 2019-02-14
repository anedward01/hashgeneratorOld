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
_m5f____ = hashFiles.md5.f
_s1_1f = hashFiles.sha1.f
_s1_224f = hashFiles.sha224.f
_s1_256f = hashFiles.sha256.f
_s1_384f = hashFiles.sha384.f
_s1_512f = hashFiles.sha512.f
_s3_224f = hashFiles.sha3_224.f
_s3_256f = hashFiles.sha3_256.f
_s3_384f = hashFiles.sha3_384.f
_s3_512f = hashFiles.sha3_512.f
_sh_128f = hashFiles.shake128.f
_sh_256f = hashFiles.shake256.f

def f(n):
    for i in range(999999):
        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        print('File Path: "' + n + '"')

        if hType == 'md5':
            _m5f____(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha1':
            _s1_1f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha224':
            _s1_224f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha256':
            _s1_256f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n
        
        elif hType == 'sha384':
            _s1_384f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha512':
            _s1_512f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3224':
            _s3_224f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3256':
            _s3_256f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3384':
            _s3_384f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3512':
            _s3_512f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'shake128':
            _sh_128f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        elif hType == 'sha3512':
            _sh_256f(n)
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

    else:
        print("Hash not found!")