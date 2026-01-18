from caesar_cipher.caesar import caesar


from caesar import caesar

def main():


    while True:
        direction = input("Type 'encode' or 'decode': ").lower()
        if direction not in ["encode", "decode"]:
            print("❌ Invalid choice")
            continue

        text = input("Type your message:\n").lower()

        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("❌ Shift must be a number")
            continue

        result = caesar(text, shift, direction)
        print(f"Here is the {direction}d result: {result}")

        if input("Again? (y/n): ").lower() == "n":
            break


if __name__ == "__main__":
    main()
