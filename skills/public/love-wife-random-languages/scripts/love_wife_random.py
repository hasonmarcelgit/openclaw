#!/usr/bin/env python3
import random

PHRASES = [
    ("English", "I love my wife."),
    ("Slovak", "Milujem moju manželku."),
    ("Czech", "Miluji svou manželku."),
    ("Spanish", "Amo a mi esposa."),
    ("French", "J'aime ma femme."),
    ("German", "Ich liebe meine Frau."),
    ("Italian", "Amo mia moglie."),
    ("Portuguese", "Eu amo minha esposa."),
    ("Polish", "Kocham moją żonę."),
    ("Japanese", "妻を愛しています。"),
    ("Korean", "저는 제 아내를 사랑합니다."),
    ("Arabic", "أنا أحب زوجتي."),
]


def main() -> None:
    picks = random.sample(PHRASES, k=3)
    for language, phrase in picks:
        print(f"{language}: {phrase}")


if __name__ == "__main__":
    main()
