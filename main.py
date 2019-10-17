import src.lib.keys as key
from src.encryption import encryption
from src.decryption import decryption

KKey = key.KKey
VKey = key.VKey

print('---------------------------------')
print('BASIC Encryption AND Decryption'.upper())
print('---------------------------------')
print('')

EOrD = input('Encryption(enc) or Decryption(dec): ')
message = input('Your encrypted or decrypted message: ')

print('')

if EOrD.upper() == 'ENC':
    print("Message:", encryption(message, KKey))
elif EOrD.upper() == 'DEC':
    print("Message:", decryption(message, VKey))

# # testing
# test = 'This is the most awesome test!'

# print(encryption(test, KKey))
# print(decryption(encryption(test, KKey), VKey))
