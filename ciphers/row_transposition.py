import math

def row_transposition_encrypt(plain_text, key):
    key_digits = [int(k) for k in key]
    len_key = len(key_digits)
    plain_text = plain_text.lower().replace(" ", "")
    len_plain = len(plain_text)

    row = math.ceil(len_plain / len_key)
    matrix = [[''] * len_key for _ in range(row)]

    # Fill the matrix row-wise
    t = 0
    for r in range(row):
        for c in range(len_key):
            if t < len_plain:
                matrix[r][c] = plain_text[t]
                t += 1

    # Determine column order based on numeric key
    col_order = [key_digits.index(i + 1) for i in range(len_key)]

    # Encrypt: Read by column order
    cipher_text = ''
    for c in col_order:
        for r in range(row):
            if matrix[r][c] != '':
                cipher_text += matrix[r][c]

    return cipher_text


def row_transposition_decrypt(cipher_text, key):
    key_digits = [int(k) for k in key]
    len_key = len(key_digits)
    len_cipher = len(cipher_text)

    row = math.ceil(len_cipher / len_key)
    matrix = [[''] * len_key for _ in range(row)]

    # Determine how many full columns each index has
    num_full_cols = len_cipher % len_key
    col_lengths = [row if i < num_full_cols else row - 1 for i in range(len_key)]

    # Determine column order
    col_order = [key_digits.index(i + 1) for i in range(len_key)]

    # Fill matrix column-wise based on order
    t = 0
    for i, c in enumerate(col_order):
        col_len = row if c < num_full_cols else row - 1
        for r in range(col_len):
            if t < len_cipher:
                matrix[r][c] = cipher_text[t]
                t += 1

    # Decrypt: Read matrix row-wise
    decrypted_text = ''
    for r in range(row):
        for c in range(len_key):
            if matrix[r][c] != '':
                decrypted_text += matrix[r][c]

    return decrypted_text
