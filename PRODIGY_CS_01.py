#  Cipher Encryption and Decryption Program

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():  # Only encrypt letters
      
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted += char  # Keep non-letters unchanged
    return encrypted

def decrypt(message, shift):
    return encrypt(message, -shift)  # Decrypt by reversing shift

def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Exiting.")
        return

    text = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            break
        except ValueError:
            print("Please enter a valid integer for shift.")

    if choice == 'E':
        result = encrypt(text, shift)
        print(f"Encrypted message: {result}")
    else:
        result = decrypt(text, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()