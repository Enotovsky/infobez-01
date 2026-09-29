ALPHABETS = (
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "abcdefghijklmnopqrstuvwxyz",
)


def shift_char(ch: str, shift: int) -> str:
    lower = ch.lower()
    for alphabet in ALPHABETS:
        idx = alphabet.find(lower)
        if idx != -1:
            new = alphabet[(idx + shift) % len(alphabet)]
            return new.upper() if ch.isupper() else new
    return ch


def encrypt(text: str, shift: int) -> str:
    return "".join(shift_char(ch, shift) for ch in text)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)


def read_shift() -> int:
    while True:
        try:
            return int(input("Введите сдвиг (целое число, можно отрицательное): "))
        except ValueError:
            print("Ошибка: сдвиг должен быть целым числом.")


def main() -> None:
    actions = {"1": ("Шифрование", encrypt), "2": ("Дешифрование", decrypt)}
    while True:
        print("\n=== Шифр Цезаря ===")
        print("1 — зашифровать")
        print("2 — расшифровать")
        print("0 — выход")
        choice = input("Выберите действие: ").strip()
        if choice == "0":
            break
        if choice not in actions:
            print("Неизвестная команда.")
            continue
        name, func = actions[choice]
        text = input("Введите текст: ")
        shift = read_shift()
        print(f"{name}, результат: {func(text, shift)}")


if __name__ == "__main__":
    main()
