def heading(headers):
    col_widths = [max(len(h), 45) for h in headers]
    total_width = sum(col_widths) + len(headers) + 1

    def print_line():
        print('+' + '+'.join('-' * w for w in col_widths) + '+')

    print_line()
    print('|' + '|'.join(h.center(w) for h, w in zip(headers, col_widths)) + '|')
    print_line()
    return col_widths, print_line

def print_row(row, col_widths):
    print('|' + '|'.join(str(val).center(w) for val, w in zip(row, col_widths)) + '|')

head = ['Username', 'Password']
col_widths, print_line = heading(head)

# Input data dari user
rows = []
username = [u for u in open('./username.txt', 'r').read().split()]
password = [p for p in open('./password.txt', 'r').read().split()]

for usr, pswd in zip(username, password):
    rows.append([usr, pswd])

# Cetak data
for row in rows:
    print_row(row, col_widths)

open('./tabel.txt', 'w').write(print_line())