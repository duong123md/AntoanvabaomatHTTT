import string

def rsa_encrypt(text, p, q, e):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    if gcd(e, phi_n) != 1:
        raise ValueError("e không nguyên tố cùng nhau với phi(n)")
    plaintext_numbers = [ord(char) for char in text]

    encrypted_numbers = [pow(m, e, n) for m in plaintext_numbers]
    
    return encrypted_numbers, n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
p = 17
q = 23
e = 5
Ten= "Bui Thi Mai Duong"

# Mã hóa
ciphertext, n = rsa_encrypt(Ten, p, q, e)
print("Ciphertext:", ciphertext)
print("n:", n)
