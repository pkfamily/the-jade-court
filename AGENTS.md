# Project preferences

- This is the user's PERSONAL GitHub repository: `pkfamily/the-jade-court`. Use the personal SSH identity through `git@github-personal:pkfamily/the-jade-court.git`. Never switch to a work GitHub account, work credentials, or a bot identity. The repository-local commit identity is `Victor Poon <10579160+pkfamily@users.noreply.github.com>` (personal account ID verified through GitHub). Before committing or pushing, verify the remote and both author and committer identities. Preserve these local overrides; do not fall back to the work email in global Git settings.

- Use OrbStack for local website previews. The user explicitly requested this on 2026-10-25. Prefer a Docker container serving `docs/` through a read-only bind mount; check available containers and images first. Keep this preference for future work in this repository.
- The site is static HTML/CSS. Prose changes should update the Markdown source and its generated HTML using the relevant script in `tools/`.
