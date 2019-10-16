import src.lib.keys as key


def decryption(string, key=key.VKey):
    dto = ''
    z = 0
    one = 0
    two = 8
    o = slice(one, two)
    b = int(len(string) / 8)
    while z < b:
        te = string[o]
        dto += key[te]
        one = one + 8
        two = two + 8
        o = slice(one, two)
        z += 1
    return dto
