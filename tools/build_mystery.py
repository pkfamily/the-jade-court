"""Render the first Mystery Players encounter using only the standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'King Poon vs Mystery players/01-The Lantern Table.md'
blocks = source.read_text().strip().split('\n\n')
title = escape(blocks[0].removeprefix('# '))
paragraphs = '\n'.join(f'        <p>{escape(block)}</p>' for block in blocks[1:])
page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="An enchanted box. A stranger in a black top hat. King Poon's next opponent has arrived. Read The Lantern Table, the first Mystery Players encounter.">
  <meta name="theme-color" content="#241b26">
  <title>King Poon vs Mystery Players — The Jade Court</title>
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body class="mystery-page">
  <a class="skip-link" href="#story-text">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="../index.html"><span class="seal" aria-hidden="true">♜</span> The Jade Court</a>
    <nav aria-label="Main navigation"><a href="../index.html#chapters">Chapters</a><a href="./" aria-current="page">Mystery Players</a></nav>
  </header>
  <main id="main">
    <section class="mystery-intro" aria-labelledby="series-title">
      <p class="eyebrow">Tales beyond the Jade Court</p>
      <h1 id="series-title">King Poon <span>vs</span><br><em>Mystery Players</em></h1>
      <p>A box opens. A stranger arrives.<br>There is always another seat at the table.</p>
      <a class="button" href="#encounter">Enter the lantern room <span aria-hidden="true">↓</span></a>
    </section>
    <figure class="mystery-art">
      <img src="../assets/images/mystery-lantern-table.jpg" width="1672" height="941" fetchpriority="high" alt="A mysterious player dressed in black with a tall black top hat faces King Poon across a bird-themed board game. A golden bird rises from an enchanted box beside them, and a glowing fireplace reveals the distant jade kingdom.">
      <figcaption>One familiar king. One unknown opponent.</figcaption>
    </figure>
    <article id="encounter" aria-labelledby="encounter-title">
      <header class="reader-header"><p class="eyebrow">Encounter 01 · The stranger in black</p><h2 id="encounter-title">TITLE</h2><p class="reading-time">4 min read</p><p class="story-note">An alternate tale inspired by “The Box” and King Poon’s journey to the Jade Court.</p></header>
      <div class="prose" id="story-text">
PARAGRAPHS
      </div>
      <footer class="chapter-end"><p class="eyebrow">The opening moves</p><p>The match is underway. Its outcome, and the stranger’s identity, remain unknown.<br>More encounters await.</p><nav class="reader-nav" aria-label="Story navigation"><a href="../index.html">← The Jade Court</a><a href="#series-title">Back to top ↑</a></nav></footer>
    </article>
  </main>
  <footer class="site-footer"><a class="brand" href="../index.html">The Jade Court</a><span>King Poon vs Mystery Players</span><a href="../story/">Poon’s backstory ↗</a></footer>
</body>
</html>
'''.replace('TITLE', title).replace('PARAGRAPHS', paragraphs)
out = ROOT / 'docs/mystery-players/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(f'Rendered {out.relative_to(ROOT)} ({len(blocks) - 1} paragraphs)')
