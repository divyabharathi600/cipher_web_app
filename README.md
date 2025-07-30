# cipher_web_app


A Streamlit-based web application to encrypt and decrypt text using classic ciphers in Information Security. This project helps users understand how various classical encryption techniques work.

---

## 🧠 Ciphers Included

### 1. 🔁 Affine Cipher
- **Formula (Encryption):** `E(x) = (a * x + b) mod 26`
- **Formula (Decryption):** `D(x) = a⁻¹ * (x - b) mod 26`
- **Key Format:** Two numbers `a` (coprime with 26) and `b`
- ✅ Validates if `a` is invertible modulo 26
- 🧾 Used in classical cryptographic applications

### 2. 🔤 Playfair Cipher
- A digraph substitution cipher using a **5x5 key matrix**
- Text is encrypted in pairs:
  - Same row ➝ Right shift
  - Same column ➝ Down shift
  - Rectangle ➝ Opposite corners
- **Key Format:** Single word (no repeats, ‘j’ is merged with ‘i’)

### 3. 🧮 Row Transposition Cipher
- A columnar transposition cipher based on **numeric key permutation**
- **Key Format:** Numeric (e.g., `31542`)
- Text is written row-wise in a matrix and read column-wise based on key order

---

## 🧰 Features

- Clean Streamlit UI
- Input validation for each cipher
- Live encryption and decryption
- Option to view cipher logic images
- Supports uppercase/lowercase conversion
- No X padding in row transposition decryption

---

## 🖼️ UI Preview
<img width="1919" height="1028" alt="Screenshot 2025-07-23 122451" src="https://github.com/user-attachments/assets/6e5a5884-6bd1-4a8f-880f-02639c60491f" />



