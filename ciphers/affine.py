def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b):
    if mod_inverse(a, 26) is None:
        return "Invalid key 'a'. Choose one coprime with 26."
    
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - base) + b) % 26) + base)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Invalid key 'a'. Choose one coprime with 26."
    
    result = ''
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - base) - b)) % 26) + base)
        else:
            result += char
    return result
