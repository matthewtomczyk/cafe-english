"""
Extract the photographs and logos used by the interactive page straight out of
the original PDF (catering.pdf), so no separate image assets have to be
prepared by hand.

Requirements:  pip install pymupdf        (Pillow is not needed)
Usage:         python3 tools/extract_images.py

Writes into ../images :
  ex-1-3-a..h.jpg    the eight coffee photos of exercise 1.3
  ex-3-13-a..h.jpg   the eight bar-equipment photos of exercise 3.13
  over-to-you-*.jpg  the picture pairs used in the "Over to you" tasks
  cover.jpg, intro-croissants.jpg, coffee-article.jpg,
  eu-logo.jpg, funded-by-eu.jpg           pictures taken from the PDF pages
"""

import os
import subprocess
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
PDF = os.path.join(BASE, "catering.pdf")
OUT = os.path.join(BASE, "images")
TMP = os.path.join(HERE, "_tmp")

os.makedirs(OUT, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

doc = pymupdf.open(PDF)


def source_pixmap(xref):
    """The raw image of a PDF xref, as a Pixmap."""
    info = doc.extract_image(xref)
    path = os.path.join(TMP, "x%d.%s" % (xref, info["ext"]))
    with open(path, "wb") as fh:
        fh.write(info["image"])
    return pymupdf.Pixmap(path)


def crop(pix, box, out_jpg):
    """box = (x0, y0, x1, y1) in source pixels; writes a JPEG."""
    x0, y0, x1, y1 = box
    src = pymupdf.open()
    page = src.new_page(width=pix.width, height=pix.height)
    page.insert_image(pymupdf.Rect(0, 0, pix.width, pix.height),
                      pixmap=pix, keep_proportion=False)
    out = pymupdf.open()
    p2 = out.new_page(width=x1 - x0, height=y1 - y0)
    p2.show_pdf_page(p2.rect, src, 0, clip=pymupdf.Rect(x0, y0, x1, y1))
    pix2 = p2.get_pixmap(dpi=72)
    png = out_jpg.replace(".jpg", ".png")
    pix2.save(png)
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                    png, "--out", out_jpg], check=True, capture_output=True)
    os.remove(png)
    print("  %s  %dx%d" % (os.path.basename(out_jpg), pix2.width, pix2.height))


def save_page(page_no, rect, out_jpg, dpi=220):
    """Crop a rectangle straight from a page of the PDF."""
    page = doc[page_no - 1]
    pix = page.get_pixmap(dpi=dpi, clip=pymupdf.Rect(*rect))
    tmp_png = out_jpg.replace(".jpg", ".png")
    pix.save(tmp_png)
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                    tmp_png, "--out", out_jpg], check=True, capture_output=True)
    os.remove(tmp_png)
    print("  %s  %dx%d" % (os.path.basename(out_jpg), pix.width, pix.height))


# ------------------------------------------------------- 1.3 : coffee photos
print("1.3 coffee photos (PDF page 12)")
pix = source_pixmap(149)
crop(pix, (0, 0, pix.width, pix.height), os.path.join(OUT, "ex-1-3-a.jpg"))

pix = source_pixmap(150)
crop(pix, (0, 1, pix.width, 288), os.path.join(OUT, "ex-1-3-b.jpg"))
crop(pix, (0, 360, pix.width, 479), os.path.join(OUT, "ex-1-3-c.jpg"))

pix = source_pixmap(151)
crop(pix, (0, 0, pix.width, 208), os.path.join(OUT, "ex-1-3-d.jpg"))
crop(pix, (0, 216, pix.width, 458), os.path.join(OUT, "ex-1-3-e.jpg"))
crop(pix, (0, 458, pix.width, 681), os.path.join(OUT, "ex-1-3-f.jpg"))
crop(pix, (0, 747, pix.width, 912), os.path.join(OUT, "ex-1-3-g.jpg"))
crop(pix, (0, 982, pix.width, 1190), os.path.join(OUT, "ex-1-3-h.jpg"))

# ------------------------------------------------- 3.13 : bar equipment photos
print("3.13 bar equipment photos (PDF page 58)")
pix = source_pixmap(323)
crop(pix, (0, 18, pix.width, 187), os.path.join(OUT, "ex-3-13-a.jpg"))
crop(pix, (0, 200, pix.width, 377), os.path.join(OUT, "ex-3-13-b.jpg"))
crop(pix, (0, 380, pix.width, 541), os.path.join(OUT, "ex-3-13-c.jpg"))
crop(pix, (0, 560, pix.width, 712), os.path.join(OUT, "ex-3-13-d.jpg"))
crop(pix, (0, 741, pix.width, 947), os.path.join(OUT, "ex-3-13-e.jpg"))

pix = source_pixmap(326)
crop(pix, (0, 0, pix.width, 224), os.path.join(OUT, "ex-3-13-f.jpg"))
pix = source_pixmap(325)
crop(pix, (0, 8, pix.width, 224), os.path.join(OUT, "ex-3-13-g.jpg"))
pix = source_pixmap(324)
crop(pix, (0, 1, pix.width, 223), os.path.join(OUT, "ex-3-13-h.jpg"))

# --------------------------------------------------- "Over to you" picture pairs
print("over-to-you pictures")
save_page(20, (115, 616, 292, 739), os.path.join(OUT, "over-to-you-unit1-1.jpg"))
save_page(20, (339, 617, 498, 737), os.path.join(OUT, "over-to-you-unit1-2.jpg"))
save_page(39, (116, 327, 351, 432), os.path.join(OUT, "over-to-you-unit2-1.jpg"))
save_page(39, (364, 327, 522, 432), os.path.join(OUT, "over-to-you-unit2-2.jpg"))
save_page(59, (106, 451, 306, 578), os.path.join(OUT, "over-to-you-unit3-1.jpg"))
save_page(59, (348, 451, 549, 576), os.path.join(OUT, "over-to-you-unit3-2.jpg"))

# ------------------------------------------------------------- single pictures
print("single pictures")
save_page(1, (88, 208, 526, 468), os.path.join(OUT, "cover.jpg"))
save_page(3, (115, 56, 531, 273), os.path.join(OUT, "intro-croissants.jpg"))
save_page(19, (387, 190, 530, 287), os.path.join(OUT, "coffee-article.jpg"))
save_page(1, (102, 45, 177, 100), os.path.join(OUT, "eu-logo.jpg"))
save_page(1, (325, 52, 514, 92), os.path.join(OUT, "funded-by-eu.jpg"))

# ------------------------------------------------------------------- favicons
print("favicons")
icon = os.path.join(BASE, "Coffee Cup Icon.png")
for size in (16, 32, 180):
    subprocess.run(["sips", "-z", str(size), str(size), icon,
                    "--out", os.path.join(OUT, "favicon-%d.png" % size)],
                   check=True, capture_output=True)
    print("  favicon-%d.png" % size)

print("done")
