def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypted message

    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted message:", encrypted_message)
    
    # Decrypted message

    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted message:", decrypted_message)


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char
    return result
if __name__ == "__main__":
    main()