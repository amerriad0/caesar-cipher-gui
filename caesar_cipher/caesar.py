import string

alphabet = string.ascii_lowercase

def caesar(text: str, shift: int, mode="encode") -> str:
    result = ""
    shift %= len(alphabet)

    if mode == "decode":
        shift *= -1

    for char in text.lower():
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char

    return result


def vigenere(text: str, key: str, mode: str = "encode") -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    key = key.lower()
    key_index = 0

    for char in text.lower():
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            if mode == "decode":
                shift *= -1
            new_index = (alphabet.index(char) + shift) % 26
            result += alphabet[new_index]
            key_index += 1
        else:
            result += char

    return result

