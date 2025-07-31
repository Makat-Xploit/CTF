UP = ord('A')
LOW = ord('a')

def Encryption(pt, key):
    ct = ''
    
    for i, p in enumerate(pt):
        if p.isupper():
            ct += chr(((ord(p) - UP) + (ord(key[i % len(key)].upper()) - UP)) % 26 + UP)
        elif p.islower():
            ct += chr(((ord(p) - LOW) + (ord(key[i % len(key)].lower()) - LOW)) % 26 + LOW)
        else:
            ct += p
    return ct

flag = ''
key = ''

print(Encryption(flag, key))