def create_matrix(key):
    key = ''.join(dict.fromkeys(key.lower().replace('j', 'i')))  # remove duplicates, replace j
    matrix = []
    used = set()
    for char in key + 'abcdefghijklmnopqrstuvwxyz':
        if char not in used and char != 'j':
            matrix.append(char)
            used.add(char)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def playfair_prepare_text(text):
    text = ''.join(filter(str.isalpha, text.lower().replace('j', 'i')))
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            pairs.append((a, 'x'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] = (pairs[-1][0], 'x')
    return pairs

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    pairs = playfair_prepare_text(text)
    result = ''

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result.upper()

def playfair_decrypt(cipher, key):
    cipher = ''.join(filter(str.isalpha, cipher.lower()))
    
    if len(cipher) % 2 != 0:
        cipher += 'x'  # pad if not even

    matrix = create_matrix(key)
    result = ''

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result.lower()
