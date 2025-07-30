from sympy import symbols, Poly
from Crypto.Util.number import bytes_to_long

flag = b"mXpCTF{}"

x = symbols('x')

chunks = [flag[i:i+2] for i in range(0, len(flag), 2)]

f_values = []
x0_values = []

for i, chunk in enumerate(chunks):
    root = bytes_to_long(chunk)
    x0 = 31337 + i
    f_values.append(str(root))
    x0_values.append(str(x0))

print("f(x) = " + ", ".join(f_values))
print("x₀   = " + ", ".join(x0_values))