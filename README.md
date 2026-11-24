# Vocational English for Catering

An interactive textbook for vocational English students in the catering and
hospitality sector, based on the EU project *"Improving Vocational English
Language Abilities for Better Performance in the Profession"*
(Project No. 2021-2-LV01-KA210-VET-000050776-P1).

**Live site:** https://matthewtomczyk.github.io/cafe-english/

## Contents

| Unit | Topic | Highlights |
|---|---|---|
| 1 | Services in a Cafe | vocabulary, readings, a listening exercise, matching, gap-fill, photo labelling, writing test |
| 2 | Services in a Restaurant | restaurant vocabulary, service situations, menus, true/false, writing test |
| 3 | Services in a Bar | bar vocabulary, the law on alcohol, cocktails, use of English (adverbs, *good*/*well*, passive voice) |
| 4 | Glossary and Useful Phrases | 111 professional terms with English definitions and Polish translations, plus useful phrases for every unit |

All exercises are interactive: the student answers in the browser and can check,
reveal or reset the answers. Notes written in the "Over to you" boxes are saved
in the browser.

## Files

```
index.html                      the interactive textbook (single page, no build step)
images/                         photos, logos, favicons and dialogue.mp3
tools/extract_images.py         regenerates images/ from catering.pdf
tools/coffee-icon.svg           vector source of the site icon
catering.pdf                    the original printed textbook
catering.md / catering.original.md   the textbook in Markdown
```

## Re-building the images

```bash
pip install pymupdf
python3 tools/extract_images.py
```

## Credits

Authors: Žilvinas Kapočius, Aurima Bajorūnienė.
Funded by the European Union. Views and opinions expressed are those of the
author(s) only and do not necessarily reflect those of the European Union or the
European Education and Culture Executive Agency (EACEA).
