---
name: love-wife-random-languages
description: Print “I love my wife” in 3 random languages. Use when the user asks for a short multilingual love phrase output.
---

# Love Wife in 3 Random Languages

Run the bundled script to print the phrase in 3 non-repeating random languages.

## Quick start

```bash
python3 scripts/love_wife_random.py
```

## Output format

- One line per language
- Format: `<Language>: <Phrase>`

Example:

- `Spanish: Amo a mi esposa.`
- `Japanese: 妻を愛しています。`
- `German: Ich liebe meine Frau.`

## Notes

- Keep exactly 3 lines unless user asks for a different count.
- Re-run for a new random set.
