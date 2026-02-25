#!/usr/bin/env python3
import random

HELLOS = [
    ("English", "Hello, world!"),
    ("Spanish", "¡Hola, mundo!"),
    ("French", "Bonjour, le monde !"),
    ("German", "Hallo, Welt!"),
    ("Italian", "Ciao, mondo!"),
    ("Portuguese", "Olá, mundo!"),
    ("Slovak", "Ahoj, svet!"),
    ("Czech", "Ahoj, světe!"),
    ("Polish", "Witaj, świecie!"),
    ("Japanese", "こんにちは、世界！"),
    ("Korean", "안녕하세요, 세상!"),
    ("Arabic", "مرحبا بالعالم!"),
]


def main() -> None:
    picks = random.sample(HELLOS, k=5)
    for language, greeting in picks:
        print(f"{language}: {greeting}")


if __name__ == "__main__":
    main()
