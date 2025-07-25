from hashlib import sha1

def BfSha1(hash: str, wordlist_path: str):
    """Bruteforce SHA1 menggunakan wordlist yang kita miliki"""
    with open(wordlist_path, 'r') as file:
        for line in file:
            if sha1(line.strip().encode()).hexdigest() == hash:
                print(f"The password is: \x1b[32m{line}\x1b[0m")
                return line
        print(f"\x1b[31mSorry, we didn't found the password\x1b[0m")


pswdHash = 'b999176d26948ba453e8ae47c36f341cfd1df525'
path = './SHAngat Aman/wordlist.txt'

BfSha1(pswdHash, path)