---
name: hello-world-random-languages
description: Generate “Hello, world!” in 5 random languages. Use when the user asks for a quick multilingual greeting demo, language variety test, or playful hello-world output.
---

# Hello World in 5 Random Languages

Run the bundled script to print 5 non-repeating random greetings.

## Quick start

```bash
python3 scripts/hello_random.py
```

## Output format

Return one line per language:

- `<Language>: <Greeting>`

Example:

- `Spanish: ¡Hola, mundo!`
- `Japanese: こんにちは、世界！`
- `Slovak: Ahoj, svet!`

## Notes

- Keep exactly 5 lines unless the user asks for a different count.
- Re-run the script for a new random set.
