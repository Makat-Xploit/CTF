from hashlib import sha1

def interface():
    print('\x1b[1;31m')
    print(r"""

  __  __       _         _      _____ _                 
 |  \/  |     | |       | |    / ____| |                
 | \  / | __ _| | ____ _| |_  | (___ | |_ ___  _ __ ___ 
 | |\/| |/ _` | |/ / _` | __|  \___ \| __/ _ \| '__/ _ \
 | |  | | (_| |   < (_| | |_   ____) | || (_) | | |  __/
 |_|  |_|\__,_|_|\_\__,_|\__| |_____/ \__\___/|_|  \___|
                                                        
    """)
    print('\x1b[1;32mSelamat datang di makat store silahkan login:\x1b[1;0m')

usr = 'Adit' ; pswd = 'b999176d26948ba453e8ae47c36f341cfd1df525' ; flag = open('./flag.txt', 'r').read()

interface()
usrLog = input("Masukkan Username : ")
usrPswd = sha1(input("Masukkan Password : ").encode()).hexdigest()

if usrLog == usr and usrPswd == pswd:
    print(f'\x1b[1;32m\nSelamat Datang! Ini flagnya : {flag}\x1b[1;0m')
elif usrLog != usr:
    print('\x1b[1;31m\nUsername salah!!\x1b[1;0m')
else:
    print('\x1b[1;31m\nPassword salah!!\x1b[1;0m')