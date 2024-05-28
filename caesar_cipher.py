def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def encrypt(text, shift):
    return caesar_cipher(text, shift, mode='encrypt')

def decrypt(text, shift):
    return caesar_cipher(text, shift, mode='decrypt')

def main():
    print("Welcome to the Caesar Cipher Program")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? (Type 'exit' to quit): ").lower()
        if choice == 'exit':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please choose 'E' for encrypt or 'D' for decrypt.")
            continue
        text = input("Enter the text: ")
        try:
            shift = int(input("Enter the shift amount (integer): "))
        except ValueError:
            print("Invalid shift amount. Please enter an integer.")
            continue
        if choice == 'e':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted text: {decrypted_text}")

def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        encrypted_text = encrypt(text, shift)
        with open(output_file, 'w') as f:
            f.write(encrypted_text)
        print(f"File encrypted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as f:
            text = f.read()
        decrypted_text = decrypt(text, shift)
        with open(output_file, 'w') as f:
            f.write(decrypted_text)
        print(f"File decrypted successfully. Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def frequency_analysis(cipher_text):
    frequency = {}
    for char in cipher_text:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)

def break_caesar_cipher(cipher_text):
    freq_analysis = frequency_analysis(cipher_text)
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'  # Frequency of letters in English
    for shift in range(26):
        decrypted_text = decrypt(cipher_text, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
