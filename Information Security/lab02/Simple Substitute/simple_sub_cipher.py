import string
import random

def generate_substitution_key():
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    return ''.join(letters)

def build_substitution_dicts(key):
    encrypt_dict = {plain: cipher for plain, cipher in zip(string.ascii_uppercase, key)}
    decrypt_dict = {cipher: plain for plain, cipher in zip(string.ascii_uppercase, key)}
    return encrypt_dict, decrypt_dict

def substitute_encrypt(text, encrypt_dict):
    result = ""
    for char in text:
        if char.isupper():
            result += encrypt_dict[char]
        elif char.islower():
            result += encrypt_dict[char.upper()].lower()
        else:
            result += char  
    return result


def substitute_decrypt(text, decrypt_dict):
    result = ""
    for char in text:
        if char.isupper():
            result += decrypt_dict[char]
        elif char.islower():
            result += decrypt_dict[char.upper()].lower()
        else:
            result += char
    return result

def encrypt_file(input_file, output_file, encrypt_dict):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    encrypted_text = substitute_encrypt(text, encrypt_dict)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)


def decrypt_file(input_file, output_file, decrypt_dict):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    decrypted_text = substitute_decrypt(text, decrypt_dict)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)


def main():
    print("Substitution Cipher File Encryption with Random Key")
    
    key = generate_substitution_key()
    print("Generated substitution key:", key)
    
    encrypt_dict, decrypt_dict = build_substitution_dicts(key)
    
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    input_file = input("Input file name: ")
    output_file = input("Output file name: ")
    
    try:
        if choice == 'e':
            encrypt_file(input_file, output_file, encrypt_dict)
            print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
        elif choice == 'd':
            decrypt_file(input_file, output_file, decrypt_dict)
            print(f"File '{input_file}' decrypted successfully to '{output_file}'.")
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")


if __name__ == "__main__":
    main()
