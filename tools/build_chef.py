"""Render The Chef's Table draft for the local static-site preview."""
from html import escape
from pathlib import Path
from math import ceil

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'chapters/drafts/the-chefs-table.md'
blocks = source.read_text().strip().split('\n\n')
title = escape(blocks[0].removeprefix('# '))
paragraphs = '\n'.join(f'        <p>{escape(block)}</p>' for block in blocks[1:])
minutes = max(1, ceil(len(' '.join(blocks[1:]).split()) / 225))
page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <meta name="description" content="King Poon meets an unexpectedly familiar face in the royal kitchens. A story draft from The Jade Court.">
  <meta name="theme-color" content="#102923">
  <title>{title} — The Jade Court</title>
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
  <a class="skip-link" href="#story-text">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="../../index.html"><span class="seal" aria-hidden="true">♜</span> The Jade Court</a>
    <nav aria-label="Main navigation"><a href="../../index.html#chapters">Chapters</a><a href="../../mystery-players/">Mystery Players</a></nav>
  </header>
  <main>
    <article aria-labelledby="chapter-title">
      <header class="reader-header"><p class="eyebrow">The Jade Court · Story draft</p><h1 id="chapter-title">{title}</h1><p class="reading-time">{minutes} min read</p><p class="story-note">A familiar face in the royal kitchens.<br>King Poon’s first meeting with Chef Curry.</p></header>
      <figure class="reader-art"><img src="../../assets/images/chefs-table-v4.jpg" width="1672" height="941" fetchpriority="high" alt="King Poon pauses in the royal kitchen doorway, recognizing Chef Curry, who turns from an iron wok in his soft white hat and cream wrap-front tunic. Steamers, ceramic bowls, and fresh ingredients fill the working kitchen."></figure>
      <div class="prose" id="story-text">
{paragraphs}
      </div>
      <footer class="chapter-end"><p class="eyebrow">End of draft</p><nav class="reader-nav" aria-label="Story navigation"><a href="../../index.html">← The Jade Court</a><a href="#chapter-title">Back to top ↑</a></nav></footer>
    </article>
  </main>
  <footer class="site-footer"><a class="brand" href="../../index.html">The Jade Court</a><span>An illustrated adventure</span><a href="../../index.html">Home ↗</a></footer>
</body>
</html>
'''
out = ROOT / 'docs/drafts/chefs-table/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(f'Rendered {out.relative_to(ROOT)}')
