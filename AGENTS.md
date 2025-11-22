# Repository Guidelines

## Project Structure & Module Organization
- Current layout: `README.md`; add application code under `src/` and tests under `tests/`.
- Keep entry points small; factor shared utilities into `src/lib/` or similar.
- Place assets and fixtures in `assets/` or `tests/fixtures/`; never commit secrets.
- Document new directories in `README.md` when added.

## Build, Test, and Development Commands
- Prefer a `Makefile` or package scripts so commands stay discoverable; mirror them in README and keep them root-relative.
- Suggested targets once tooling exists:
  - `make run` (or direct runtime call such as `python src/main.py` / `node src/index.js`) to execute the app.
  - `make test` for the full suite; keep it non-interactive and deterministic.
  - `make lint` for formatting/linting before pushing.
- Avoid environment-specific flags in default targets; keep paths portable.

## Coding Style & Naming Conventions
- Use UTF-8 with LF endings; spaces over tabs (2 for JS/TS, 4 for Python).
- Name files with kebab-case or snake_case; reserve PascalCase for exported classes/types.
- Adopt standard formatters (Prettier, Black, gofmt) and check in their configs.
- Keep functions small and pure where possible; document public APIs with brief docstrings/comments.

## Testing Guidelines
- Co-locate tests in `tests/`, mirroring `src/` paths; name files `*_test.*` or `*.spec.*`.
- Choose a mainstream framework (pytest, jest, go test) and pin versions in lockfiles.
- Add focused, deterministic tests for new behaviors and at least one negative case.
- Include usage examples or fixtures for new endpoints/CLIs in `tests/fixtures/`.
- Run the full suite before submitting; include coverage flags if available.

## Commit & Pull Request Guidelines
- History is minimal (`Initial commit`); use imperative, scoped messages, e.g., `feat: add greeting cli` or `fix: handle empty input`.
- Keep PRs small and focused; include a summary, testing notes (e.g., `make test` output), and screenshots/CLI samples when UX changes.
- Reference issue IDs when applicable; call out breaking changes explicitly with upgrade notes.

## Security & Configuration Tips
- Do not commit secrets; use `.env.example` for configuration templates.
- Prefer environment variables for credentials and ports; document defaults in `README.md`.
- Validate inputs and add logging for error paths as the project grows.
