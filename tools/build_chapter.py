"""Render the Chapter 1 prose draft as static HTML (Python standard library only)."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'chapters/01-a-dunk-through-heaven.md'
blocks = source.read_text().strip().split('\n\n')
title = blocks[0].removeprefix('# Chapter 1: ')
paragraphs = '\n'.join(f'      <p>{escape(block)}</p>' for block in blocks[1:])
page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="An impossible dunk carries King James into an unfamiliar kingdom. Read Chapter 1 of The Jade Court.">
  <meta name="theme-color" content="#102923">
  <title>Chapter 1: TITLE — The Jade Court</title>
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body>
  <a class="skip-link" href="#story-text">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="../../index.html" aria-label="The Jade Court home"><span class="seal" aria-hidden="true">♜</span> The Jade Court</a>
    <nav aria-label="Main navigation"><a href="../../index.html#chapters">All chapters</a><a href="../../story/">Full story</a></nav>
  </header>
  <main id="main">
    <article aria-labelledby="chapter-title">
      <header class="reader-header"><p class="eyebrow">The Jade Court · Chapter 01</p><h1 id="chapter-title">TITLE</h1><p class="reading-time">3 min read</p></header>
      <figure class="reader-art"><img src="../../assets/images/space-rift.jpg" width="1672" height="941" fetchpriority="high" alt="King James slams the ball through the hoop. A golden rift tears open above him, revealing jade palaces and emerald mountains beyond the basketball arena."></figure>
      <div class="prose" id="story-text">
PARAGRAPHS
      </div>
      <footer class="chapter-end"><p class="eyebrow">End of Chapter 01</p><p>King Poon’s adventure has only just begun.<br>More chapters to come.</p><nav class="reader-nav" aria-label="Chapter navigation"><a href="../../index.html#chapters">← All chapters</a><a href="#chapter-title">Back to top ↑</a></nav></footer>
    </article>
  </main>
  <footer class="site-footer"><a class="brand" href="../../index.html">The Jade Court</a><span>An illustrated adventure</span><a href="../../index.html">Home ↗</a></footer>
</body>
</html>
'''.replace('TITLE', escape(title)).replace('PARAGRAPHS', paragraphs)
out = ROOT / 'docs/chapters/01/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(f'Rendered {out.relative_to(ROOT)} ({len(blocks) - 1} paragraphs)')
