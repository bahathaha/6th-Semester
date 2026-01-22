def caesar_encrypt(text, key):
    key %= 26
    encrypted_text = ""
    
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + key) % 26 + base)
        elif char == ' ' or char == '\n':
            encrypted_text += char
        else:
            raise ValueError(f"Invalid character in input: {char}")
    return encrypted_text


def caesar_decrypt(text, key):
    key %= 26
    decrypted_text = ""
    
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - key) % 26 + base)
        elif char == ' ' or char == '\n':
            decrypted_text += char
        else:
            raise ValueError(f"Invalid character in input: {char}")
    return decrypted_text


def encrypt_file(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    encrypted_text = caesar_encrypt(text, key)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    decrypted_text = caesar_decrypt(text, key)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

def main():
    print("Caesar Cipher File Encryption")
    choice = input("Do you want to Encrypt or Decrypt? (e/d): ").lower()
    input_file = input("Input file name: ")
    output_file = input("Output file name: ")
    key = 3
    
    try:
        if choice == 'e':
            encrypt_file(input_file, output_file, key)
            print(f"File '{input_file}' encrypted successfully to '{output_file}'.")
        elif choice == 'd':
            decrypt_file(input_file, output_file, key)
            print(f"File '{input_file}' decrypted successfully to '{output_file}'.")
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
