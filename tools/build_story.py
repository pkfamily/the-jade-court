"""Render the original V1 story as static HTML, using only the standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
blocks = (ROOT / 'story.md').read_text().strip().split('\n\n')
paragraphs = '\n'.join(f'        <p>{escape(block)}</p>' for block in blocks if not block.startswith('#'))
page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Read the original story of King Poon: a basketball champion transported to a kingdom devoted to board games.">
  <meta name="theme-color" content="#102923">
  <title>The Full Story — The Jade Court</title>
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <a class="skip-link" href="#story-text">Skip to story</a>
  <header class="site-header">
    <a class="brand" href="../index.html" aria-label="The Jade Court home"><span class="seal" aria-hidden="true">♜</span> The Jade Court</a>
    <nav aria-label="Main navigation"><a href="../index.html#chapters">Chapters</a><a href="../index.html">Home</a></nav>
  </header>
  <main id="main">
    <article aria-labelledby="story-title">
      <header class="reader-header"><p class="eyebrow">The original story · V1</p><h1 id="story-title">The Jade Court</h1><p class="reading-time">The complete tale · 3 min read</p><p class="story-note">Includes the ending. The chapters expand on this original tale.</p></header>
      <figure class="reader-art"><img src="../assets/images/jade-throne.jpg" width="1672" height="941" fetchpriority="high" alt="King Poon on his jade dragon throne, with a basketball-topped scepter and a royal Go board beside him."></figure>
      <div class="prose" id="story-text">
PARAGRAPHS
      </div>
      <footer class="chapter-end"><p class="eyebrow">The end</p><p>Explore King Poon’s adventures in the chapters.</p><nav class="reader-nav" aria-label="Story navigation"><a href="../chapters/01/">Read Chapter 1 ↗</a><a href="../index.html#chapters">All chapters</a></nav></footer>
    </article>
  </main>
  <footer class="site-footer"><a class="brand" href="../index.html">The Jade Court</a><span>An illustrated adventure</span><a href="#story-title">Back to top ↑</a></footer>
</body>
</html>
'''.replace('PARAGRAPHS', paragraphs)
out = ROOT / 'docs/story/index.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page)
print(f'Rendered {out.relative_to(ROOT)}')
