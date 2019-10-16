import src.lib.keys as key
from src.encryption import encryption
from src.decryption import decryption

KKey = key.KKey
VKey = key.VKey
test = 'This is the most awesome test!'

print(encryption(test, KKey))
print(decryption(encryption(test, KKey), VKey))
