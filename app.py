import streamlit as st
from ciphers.rail_fence import rail_fence_encrypt, rail_fence_decrypt
from ciphers.row_transposition import row_transposition_encrypt, row_transposition_decrypt
from ciphers.caesar import caesar_encrypt, caesar_decrypt
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.affine import affine_encrypt, affine_decrypt
from ciphers.playfair import playfair_encrypt, playfair_decrypt

st.title("🔐 Cipher Web App - Classical Encryption Suite")

cipher_choice = st.selectbox("Choose a Cipher", [
    "Rail Fence Cipher",
    "Row Transposition Cipher",
    "Caesar Cipher",
    "Vigenère Cipher",
    "Affine Cipher",
    "Playfair Cipher"
])

operation = st.radio("Choose Operation", ["Encrypt", "Decrypt"])
text = st.text_input("Enter your text")

if cipher_choice == "Rail Fence Cipher":
    key = st.number_input("Number of Rails", min_value=2, step=1)
    if st.button("Submit"):
        result = rail_fence_encrypt(text, int(key)) if operation == "Encrypt" else rail_fence_decrypt(text, int(key))
        st.success(f"Result: {result}")

elif cipher_choice == "Row Transposition Cipher":
    key = st.text_input("Enter Numeric Key (e.g., 31542)")
    if key.isdigit():
        if st.button("Submit"):
            result = row_transposition_encrypt(text, key) if operation == "Encrypt" else row_transposition_decrypt(text, key)
            st.success(f"Result: {result}")
    else:
        st.warning("Please enter a numeric key only.")


elif cipher_choice == "Caesar Cipher":
    shift = st.number_input("Enter Shift Value", step=1)
    if st.button("Submit"):
        result = caesar_encrypt(text, int(shift)) if operation == "Encrypt" else caesar_decrypt(text, int(shift))
        st.success(f"Result: {result}")

elif cipher_choice == "Vigenère Cipher":
    key = st.text_input("Enter Key (alphabetic only)")
    if key.isalpha() and st.button("Submit"):
        result = vigenere_encrypt(text, key) if operation == "Encrypt" else vigenere_decrypt(text, key)
        st.success(f"Result: {result}")
    elif not key.isalpha():
        st.warning("Key should be alphabetic only.")

elif cipher_choice == "Affine Cipher":
    a = st.number_input("Enter 'a' (must be coprime with 26)", step=1)
    b = st.number_input("Enter 'b'", step=1)
    if st.button("Submit"):
        result = affine_encrypt(text, int(a), int(b)) if operation == "Encrypt" else affine_decrypt(text, int(a), int(b))
        st.success(f"Result: {result}")

elif cipher_choice == "Playfair Cipher":
    key = st.text_input("Enter Key (alphabetic only)")
    if key.isalpha() and st.button("Submit"):
        result = playfair_encrypt(text, key) if operation == "Encrypt" else playfair_decrypt(text, key)
        st.success(f"Result: {result}")
    elif not key.isalpha():
        st.warning("Key should be alphabetic only.")
