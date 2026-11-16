def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result
def decrypt(text,shift):
    return encrypt(text, -shift)
while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Choose an option:")
    if choice == '1':
        message = input("Enter message:")
        shift = int(input("Enter shift amount:"))
        print(f"  Encrypted text: {encrypt(message,shift)}")
    elif choice == '2':
        message = input("Enter message:")
        shift = int(input("Enter shift amount:"))
        print(f" Decrypted text: {decrypt(message,shift)}")
    elif choice == '3':
        print("Good bye!")
        break