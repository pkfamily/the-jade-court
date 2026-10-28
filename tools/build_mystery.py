"""Render the Mystery Players encounter and its continuation using only the standard library."""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'King Poon vs Mystery players/01-The Lantern Table.md'
blocks = source.read_text().strip().split('\n\n')
title = escape(blocks[0].removeprefix('# '))
rendered = []
for block in blocks[1:]:
    illustration = re.fullmatch(r'!\[(.*?)\]\((.*?)\)', block)
    if illustration:
        alt, relative_path = illustration.groups()
        image_path = (source.parent / relative_path).resolve()
        web_path = image_path.relative_to(ROOT / 'docs')
        rendered.append(
            f'        <figure class="story-illustration"><img src="../{escape(web_path.as_posix())}" '
            f'width="1672" height="941" loading="lazy" alt="{escape(alt)}">'
            '<figcaption>Through the box, into another world. The golden bird leads the way.</figcaption></figure>'
        )
    else:
        rendered.append(f'        <p>{escape(block)}</p>')
paragraphs = '\n'.join(rendered)
continuation = ROOT / 'King Poon vs Mystery players/02-The Birds Beneath.md'
continuation_blocks = continuation.read_text().strip().split('\n\n')
continuation_title = escape(continuation_blocks[0].removeprefix('# '))
continuation_paragraphs = '\n'.join(
    f'        <p>{escape(block)}</p>' for block in continuation_blocks[1:]
)
continuation_minutes = max(1, round(len(continuation.read_text().split()) / 200))
continuation_article = f'''    <article id="the-birds-beneath" aria-labelledby="continuation-title">
      <header class="reader-header"><p class="eyebrow">Encounter 01 · Part two</p><h1 id="continuation-title">{continuation_title}</h1><p class="reading-time">{continuation_minutes} min read</p><p class="story-note">A fictional retelling of Wingspan replay #937896051.</p></header>
      <div class="prose" id="story-text">
{continuation_paragraphs}
      </div>
      <footer class="chapter-end"><p class="eyebrow">End of the first match</p><p>The name in the register can wait. There is a game to learn from.</p><nav class="reader-nav" aria-label="Continuation navigation"><a href="../">← The Lantern Table</a><a href="../../index.html">The Jade Court →</a></nav></footer>
    </article>'''
page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="An enchanted box. A stranger in a black top hat. King Poon's next opponent has arrived. Read The Lantern Table and The Birds Beneath, the first Mystery Players encounter.">
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
    <nav class="episode-list" aria-label="Encounter 01 reading order">
      <ol>
        <li><a href="#encounter"><span>The Lantern Table</span><small>The stranger arrives.</small></a></li>
        <li><a href="the-birds-beneath/"><span>The Birds Beneath</span><small>The match unfolds.</small></a></li>
      </ol>
    </nav>
    <figure class="mystery-art">
      <img src="../assets/images/mystery-lantern-table-v4.jpg" width="1672" height="941" fetchpriority="high" alt="A mysterious player dressed in black with a tall black top hat faces King Poon across a bird-themed board game. Tall jade columns and an empty dragon throne rise behind Poon. A golden bird hovers above an enchanted box, and a monumental jade hearth reveals a sunlit kingdom.">
      <figcaption>One familiar king. One unknown opponent.</figcaption>
    </figure>
    <article id="encounter" aria-labelledby="encounter-title">
      <header class="reader-header"><p class="eyebrow">Encounter 01 · The stranger in black</p><h2 id="encounter-title">TITLE</h2><p class="reading-time">4 min read</p><p class="story-note">An alternate tale inspired by “The Box” and King Poon’s journey to the Jade Court.</p></header>
      <div class="prose" id="story-text">
PARAGRAPHS
      </div>
      <footer class="chapter-end"><p class="eyebrow">The opening moves</p><p>The tea is cooling, and the stranger is remembering how to play.</p><nav class="reader-nav" aria-label="Story navigation"><a href="../index.html">← The Jade Court</a><a href="the-birds-beneath/">Continue: The Birds Beneath →</a></nav></footer>
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

continuation_page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="The stranger's wetland fills with birds, and King Poon discovers how much can hide beneath the cards. Part two of the first Mystery Players encounter.">
  <meta name="theme-color" content="#241b26">
  <title>{continuation_title} — Mystery Players — The Jade Court</title>
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../assets/style.css">
</head>
<body class="mystery-page">
  <a class="skip-link" href="#story-text">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="../../index.html"><span class="seal" aria-hidden="true">♜</span> The Jade Court</a>
    <nav aria-label="Main navigation"><a href="../../index.html#chapters">Chapters</a><a href="../">Mystery Players</a></nav>
  </header>
  <main id="main">
    <figure class="mystery-art">
      <img src="../../assets/images/mystery-wetland-flocks-v5.jpg" width="1672" height="941" fetchpriority="high" alt="Five prominent birds and a few smaller flock companions gather above glowing stacks of tucked bird cards and moonlit reeds beneath the lanterns of an empty jade pavilion.">
      <figcaption>Between the cards, a wetland comes alive.</figcaption>
    </figure>
{continuation_article}
  </main>
  <footer class="site-footer"><a class="brand" href="../../index.html">The Jade Court</a><span>King Poon vs Mystery Players</span><a href="../">The Lantern Table ↗</a></footer>
</body>
</html>
'''
continuation_out = ROOT / 'docs/mystery-players/the-birds-beneath/index.html'
continuation_out.parent.mkdir(parents=True, exist_ok=True)
continuation_out.write_text(continuation_page)
print(f'Rendered {continuation_out.relative_to(ROOT)}')
