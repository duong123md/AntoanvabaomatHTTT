def caesar_cipher(plaintext, k):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = k % 26
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char  

    return result
k = 7  
plaintext = "Bui Thi Mai Duong"
ciphertext = caesar_cipher(plaintext, k)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)