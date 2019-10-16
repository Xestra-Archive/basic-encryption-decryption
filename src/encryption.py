import src.lib.keys as key


def encryption(string, key=key.KKey):
    eto = ''
    for x in string:
        eto += key[x]
    return eto
