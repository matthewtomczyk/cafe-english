# Tools

## `extract_images.py`
Regenerates everything in `../images` straight from `../catering.pdf`:

```bash
pip install pymupdf
python3 tools/extract_images.py
```

| Output | Source |
|---|---|
| `ex-1-3-a..h.jpg` | the eight coffee photos of exercise 1.3 (PDF page 12) |
| `ex-3-13-a..h.jpg` | the eight bar-equipment photos of exercise 3.13 (PDF page 58) |
| `over-to-you-unit{1,2,3}-{1,2}.jpg` | the picture pairs of the "Over to you" tasks |
| `cover.jpg`, `intro-croissants.jpg`, `coffee-article.jpg` | single pictures from the book |
| `eu-logo.jpg`, `funded-by-eu.jpg` | the EU funding logos from the cover |
| `favicon-16/32/180.png` | scaled from `../Coffee Cup Icon.png` |

Requires PyMuPDF; the JPEG re-encoding uses macOS `sips`.

## `coffee-icon.svg`
Vector source of the site icon (yellow rounded square, navy coffee cup). Render it
at any size, e.g. with headless Chrome:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --default-background-color=00000000 --window-size=1254,1254 \
  --screenshot="Coffee Cup Icon.png" tools/coffee-icon.svg
```
