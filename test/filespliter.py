# Write our file splitting program here

import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3
 
# initiating the "s" object to use the
# sha3_224 algorithm from the hashlib module.
s = hashlib.sha3_256()

# providing the input to the hashing algorithm.
s.update(b"Hello World")

print("Hellow World")
print("Sha3_256 :"+ s.hexdigest())
