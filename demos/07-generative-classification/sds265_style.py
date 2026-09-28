"""Shared plotting style for S&DS 265 slide figures.

Every lecture figure script imports this module so that all decks share one
visual language and so that figures are generated at their true on-slide size.

The sizing rule is the important part.  A Beamer frame in this course has

    textwidth  = 406.87 pt = 5.63 in
    textheight = 223.00 pt = 3.09 in

A figure must therefore be created at the width it will actually occupy and
inserted at scale 1.  Generating a 9.6 in figure and inserting it at
``0.8\\linewidth`` shrinks every label to about half its nominal size, which is
what made the earlier decks unreadable when projected.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# --- Course palette (matches theme/yale-white-beamer.tex) --------------------
BLUE = "#00356B"
BLUE_BRIGHT = "#286DC0"
RED = "#7A3E47"
GREEN = "#5B7864"
INK = "#202A35"
MUTED = "#66727E"
RULE = "#D8E0E8"
BLUE_PALE = "#F2F6FA"

# Muted fills for large filled areas (bars, bands, blocks).  The line palette
# above is fine for strokes, but Yale navy at full saturation overwhelms a page
# when it fills half of it.  These are desaturated to sit with RED and GREEN,
# which are already muted.
# These now point at the Morandi series colors below, so every figure that
# fills an area picks up the new palette without editing its generator.
BLUE_FILL = "#8C9FB1"
RED_FILL = "#B0846F"
GREEN_FILL = "#9AAE96"

# Histogram convention used in both the slides and the reading notes.  Bars
# use a muted fill so a large inked area does not dominate the page, while the
# darker outline keeps adjacent bins legible.  Comparative histograms use the
# red companion rather than introducing a lecture-specific color.
HISTOGRAM_PRIMARY = {
    "color": BLUE_FILL,
    "edgecolor": "#5C7186",
    "linewidth": 0.8,
    "alpha": 0.88,
}
HISTOGRAM_SECONDARY = {
    "color": RED_FILL,
    "edgecolor": "#835747",
    "linewidth": 0.8,
    "alpha": 0.78,
}

# --- Morandi series palette -------------------------------------------------
#
# The semantic colors above carry meaning: navy is structure, red is caution,
# green is evidence.  They are the wrong tool for *categorical* series, because
# navy and BLUE_FILL differ mainly in lightness and both sit close to the ink
# the surrounding text is set in -- a navy bar beside a grey-blue bar, under a
# navy title, gives the eye nothing to separate.
#
# These are low-chroma, mid-tone hues in the manner of Morandi's palettes.  They
# separate by HUE rather than by lightness, so adjacent categories stay legible
# when projected, and none of them competes with the body text.  Use them for
# data series; keep navy/red/green for what things MEAN.
MORANDI_BLUE = "#8C9FB1"    # dusty blue
MORANDI_CLAY = "#B0846F"    # terracotta, the warm counterweight to the blue
MORANDI_SAGE = "#9AAE96"    # muted green
MORANDI_MAUVE = "#A98FA0"   # dusty plum
MORANDI_SAND = "#C7B392"    # pale ochre
MORANDI_STONE = "#8A8F8A"   # neutral, for a series that should recede

#: Categorical order for series that carry no intrinsic meaning.
MORANDI = [MORANDI_BLUE, MORANDI_CLAY, MORANDI_SAGE,
           MORANDI_MAUVE, MORANDI_SAND, MORANDI_STONE]

#: Slightly darkened companions, for the stroke around a filled shape or for a
#: line drawn on top of one.  A fill plus its own darker edge reads far better
#: than a fill plus the navy used for titles.
MORANDI_EDGE = {
    MORANDI_BLUE: "#5C7186",
    MORANDI_CLAY: "#835747",
    MORANDI_SAGE: "#6B8067",
    MORANDI_MAUVE: "#7C6373",
    MORANDI_SAND: "#9A8763",
    MORANDI_STONE: "#5F645F",
}


# The default cycle for unlabelled series.  Previously navy/red/green, which
# put data lines in the same colors as the frame titles and the emphasis spans;
# the Morandi hues sit clearly below the text in weight.
CYCLE = MORANDI

# --- Canonical figure sizes, in inches, measured from the frame -------------
TEXTWIDTH = 5.63
TEXTHEIGHT = 3.09

# A frame title costs about 37pt on top of TEXTHEIGHT, so a one-line-title
# frame really offers 186pt (2.57in).  These sizes are what is left after the
# caption block each macro adds; see \sdsframebody in theme/lecture-macros.tex.

#: Figure shown by \figtakeaway: takeaway line plus source credit beneath.
FULL = (TEXTWIDTH, 2.00)
#: Figure shown by \fullfig: source credit only.
FULL_TALL = (TEXTWIDTH, 2.35)
#: Short banner figure, for a strip of panels above supporting text.
FULL_SHORT = (TEXTWIDTH, 1.70)
#: One column of a two-column frame (0.48 textwidth).
HALF = (2.70, 2.05)
#: One column of a two-column frame, full height.
HALF_TALL = (2.70, 2.45)

_BASE_FONT = 9.0


def _register_pagella() -> bool:
    """Make TeX Gyre Pagella available to matplotlib, if TeX Live has it.

    The slides are typeset in TeX Gyre Pagella by fontspec/unicode-math.  Left
    to itself matplotlib picks macOS Palatino for figure text and STIX --- a
    Times-metric face --- for figure math, so a single frame could show three
    different letterforms.  Registering the actual OTFs lets figures use the
    same family as the surrounding slide, for text and for math.

    macOS Palatino is not a substitute: it ships as one .ttc that matplotlib
    registers with style=normal only, so mathtext renders variables upright.
    """
    import glob
    from matplotlib import font_manager

    faces = []
    for pattern in (
        "/usr/local/texlive/*/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-*.otf",
        "/usr/share/texlive/*/texmf-dist/fonts/opentype/public/tex-gyre/texgyrepagella-*.otf",
        str(Path.home() / "Library/Fonts/texgyrepagella-*.otf"),
    ):
        faces.extend(glob.glob(pattern))
    if not faces:
        return False
    for face in faces:
        try:
            font_manager.fontManager.addfont(face)
        except Exception:                                  # noqa: BLE001
            return False
    # The decks set code in JetBrains Mono; register it too so a figure that
    # shows a literal string matches the listings on the slides.
    for pattern in (
        "/usr/local/texlive/*/texmf-dist/fonts/opentype/SIL/jetbrainsmono-otf/JetBrainsMono-Regular.otf",
        "/usr/share/texlive/*/texmf-dist/fonts/opentype/SIL/jetbrainsmono-otf/JetBrainsMono-Regular.otf",
        str(Path.home() / "Library/Fonts/JetBrainsMono-Regular.otf"),
    ):
        for face in glob.glob(pattern):
            try:
                font_manager.fontManager.addfont(face)
            except Exception:                              # noqa: BLE001
                pass
    return any(f.name == "TeX Gyre Pagella"
               for f in font_manager.fontManager.ttflist)


_HAS_PAGELLA = _register_pagella()

#: Math is set in the same family as the text when Pagella is available.  The
#: fallback keeps the previous behaviour so a machine without TeX Live still
#: renders every figure.
_MATH = (
    {
        "mathtext.fontset": "custom",
        "mathtext.rm": "TeX Gyre Pagella",
        "mathtext.it": "TeX Gyre Pagella:italic",
        "mathtext.bf": "TeX Gyre Pagella:bold",
        "mathtext.cal": "TeX Gyre Pagella:italic",
        "mathtext.sf": "TeX Gyre Pagella",
    }
    if _HAS_PAGELLA
    else {"mathtext.fontset": "stix"}
)

#: Text stays on macOS Palatino, which is what fontspec gives the slides, so
#: figure prose and slide prose are the same face.  Only the math families
#: above move to Pagella, whose letterforms match Pagella Math -- the font
#: unicode-math sets every equation on the slides in.
_SERIF = ["Palatino", "TeX Gyre Pagella", "STIXGeneral", "DejaVu Serif"]


def use_course_style() -> None:
    """Apply the course rcParams.  Call once at the top of a figure script."""
    mpl.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": _SERIF,
            "font.monospace": ["JetBrains Mono", "Menlo", "DejaVu Sans Mono"],
            **_MATH,
            "font.size": _BASE_FONT,
            "axes.titlesize": _BASE_FONT + 0.5,
            "axes.labelsize": _BASE_FONT,
            # Nothing below 8pt: a label that is unreadable when projected is
            # worse than no label, because it still costs space and attention.
            "xtick.labelsize": _BASE_FONT - 1.0,
            "ytick.labelsize": _BASE_FONT - 1.0,
            "legend.fontsize": _BASE_FONT - 1.0,
            "axes.titlecolor": BLUE,
            "axes.labelcolor": INK,
            "axes.edgecolor": MUTED,
            "axes.linewidth": 0.7,
            "axes.grid": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.prop_cycle": cycler(color=MORANDI),
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "lines.linewidth": 1.8,
            "legend.frameon": False,
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
            "savefig.bbox": "tight",
            # A small, uniform pad keeps the inserted PDF flush with the text
            # block instead of floating inside stray whitespace.
            "savefig.pad_inches": 0.02,
            "pdf.fonttype": 42,
        }
    )


def save(fig, path: Path | str, notes_svg: Path | str | None = None) -> Path:
    """Write a figure as vector PDF for the deck, and optionally SVG for the notes.

    The Quarto lecture notes render to HTML and take SVG, while the Beamer deck
    takes PDF.  Emitting both from the same call keeps a figure from drifting
    between the two.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    if notes_svg is not None:
        notes_svg = Path(notes_svg)
        notes_svg.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(notes_svg)
    plt.close(fig)
    return path
