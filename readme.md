# The Jade Court

A webcomic in development about a basketball champion transported to a kingdom where board games shape culture, power, and diplomacy.

Now ruling as King Poon, he brings a champion's instincts to Go, Xiangqi, and the kingdom's own games—while finding his place in an unfamiliar world.

## Project status

Early story development. The [original story (V1)](story.md) is the foundation and overarching synopsis. Individual chapters expand its events while preserving its playful, larger-than-life tone. Neighboring realms inspired by Wingspan, Dune, The Castles of Burgundy, and Ark Nova can emerge through later adventures.

Start reading [Chapter 1: A Dunk Through Heaven](chapters/01-a-dunk-through-heaven.md). This is a prose draft, ready for review before adaptation into comic pages.

The website also includes the [complete original V1 story](docs/story/index.html), with its ending, linked from the landing page and chapter reader. Edit `story.md` and run `python3 tools/build_story.py` to update that page without changing the original prose.

The [V2 experiment](story-v2.md) is retained as a source of optional ideas, rather than the main storyline. A static reader website now lives in `docs/`, with a landing page, chapter archive, and illustrated Chapter 1. Sequential comic panels are still to come. The story synopses contain plot spoilers.

## Getting started

Open [docs/index.html](docs/index.html) directly in a browser, or serve the website locally:

```sh
python3 -m http.server 8000 --directory docs
```

Then visit `http://localhost:8000`. The site uses plain HTML and CSS, with local images and system fonts; it needs no package installation or JavaScript.

Edit `chapters/01-a-dunk-through-heaven.md` for Chapter 1 prose, then run `python3 tools/build_chapter.py` to update the reader HTML. Commit the generated HTML along with the source. Python 3.9+ is needed only for this rendering step or the optional local server. Layout and styles live in `docs/index.html`, `tools/build_chapter.py`, and `docs/assets/style.css`.

## Webcomic workflow

1. **Write:** Break the story into episodes, then script each page or scrolling sequence. Track episode tasks with GitHub Issues.
2. **Draw:** Develop thumbnails, artwork, lettering, and final exports. Keep large layered originals in a backed-up art archive; commit optimized web images to this repository.
3. **Prepare:** Give each episode a stable number and URL. Include its title, reading order, image descriptions, and a text transcript.
4. **Review:** Work on an episode branch and open a pull request. Preview the reader on mobile and desktop; check lettering, image loading, transcripts, and previous/next links.
5. **Publish:** Merge the finished episode into `main` and deploy the reader website through GitHub Pages. This deployment still needs to be configured.
6. **Maintain:** Correct typos and broken links through normal commits. Keep published episode URLs stable.

For solo work, branches and pull requests are optional, but they provide a useful final review before publishing.

## Repository layout

The production sources and public website are organized as follows:

```text
story.md                    # V1: foundation and overarching synopsis
story-v2.md                 # Alternate experiment; optional ideas
chapters/                   # Prose chapters expanding V1
assets/images/              # Original generated artwork and prompts
references/                 # Character reference
tools/build_chapter.py      # Renders the Chapter 1 draft to HTML
docs/                       # Public reader website (GitHub Pages source)
  index.html                # Landing page and episode archive
  chapters/01/index.html    # Chapter 1 reader
  assets/                  # Shared CSS, favicon, and optimized JPEGs
```

Use numbered image filenames such as `001-01.webp` and `001-02.webp` to make reading order clear. Keep private notes and unreleased material outside a public repository: files outside `docs/` are still visible on GitHub.

## Publishing with GitHub Pages

The site uses relative links so it can run under a GitHub Pages repository URL. The first chapter links back to the archive; future chapter navigation can be added as chapters are published.

Once this repository has been pushed to GitHub:

1. Open **Settings → Pages**.
2. Select **Deploy from a branch**, then `main` and `/docs`.
3. Save and check the deployment result before sharing the site.

`docs/.nojekyll` is included to publish the plain HTML without Jekyll processing. If the comic later needs a static site generator, GitHub Actions can build and publish it instead.

See GitHub's [publishing source documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). Keep exported images reasonably sized as the archive grows.

## Next milestones

- Review Chapter 1 and adapt it into a comic script.
- Establish character designs and the visual style.
- Choose page-based or vertical-scroll reading.
- Produce the first episode and its transcript.
- Review the reader website and enable GitHub Pages.

## Visual references

[King Poon visual reference](references/king-poon-visual-reference.webp), supplied as inspiration for character development. Source and usage rights have not yet been recorded.

Generated artwork drafts:

- [King Poon on the jade throne](assets/images/king-poon-jade-throne-v1.png): landing-page artwork with a Go-board dais and royal strategy table.
- [The dunk that opens a rift](assets/images/dunk-space-rift-v1.png): Chapter 1 artwork showing the kingdom through a golden tear above the rim.

Both images were created with the built-in image generation tool using the character reference. The [generation prompts](assets/images/generation-prompts.txt) are saved for future revisions.

## Licensing

No license has been selected yet. Before publication, decide how the story and artwork may be reused, and whether future website code should have a separate license. Record credits and license requirements for any third-party assets.
