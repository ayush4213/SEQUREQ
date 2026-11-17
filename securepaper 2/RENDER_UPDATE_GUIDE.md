# Update the existing SecurePaper site on Render

Site provided by the owner: https://secure-ques-q.onrender.com/

This archive contains the full application, not a replacement service or a new design. The user-facing copy/sections were cleaned up in `frontend/app.js` and `frontend/index.html`; **no CSS, question-selection logic, database schema, scoring, API route or authentication logic was changed**.

## Deploy these changes to the EXISTING Render service

1. Back up your current application repository and **the live database**. Do not replace the live SQLite file with the bundled `data/securepaper.db` if you need to keep imported MCQs, admin edits or existing student sessions.
2. In the repository connected to the **existing** Render service, update the source files with this archive's `securepaper/` contents. If the hosted repository has other changes made since the uploaded project version, apply `UI_ONLY_PATCH.diff` to its frontend instead of overwriting newer code. Keep the existing git history, remote, and service settings. The main runtime files are `frontend/app.js`, `frontend/index.html`, `backend/main.py`, `backend/selector.py`, `backend/schema.sql`, `seed/seed_questions.json`, `requirements.txt`, `Dockerfile`, and `start.sh`.
3. If your service uses the supplied Dockerfile, the existing `start.sh` runs Uvicorn with `$PORT`. If it uses a native Python runtime instead, keep its current start command (for example: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`).
4. Retain the Render environment variables, including the real `SECUREPAPER_ADMIN_KEY` and `SECUREPAPER_DATA_DIR`. Ensure the latter points to the currently mounted persistent disk if you have one. This package has no real admin secret.
5. Commit and push to the git branch watched by your existing Render Web Service, or deploy the updated source using your current Render workflow. Trigger **Manual Deploy** on that service if it does not auto-deploy.
6. Once deployed, check `https://secure-ques-q.onrender.com/api/health`, then load the home page, generate an exam, navigate MCQs, submit, view the result, sign in to Question Bank and inspect Sessions. The UI text removals should be visible after a hard refresh.

**Do not use the optional `render.yaml` to create a new Blueprint** when the goal is to replace the code behind the current `secure-ques-q` URL. The optional YAML describes a new example service (`securepaper-mcq-demo`) and will not automatically update an unrelated existing service.

## Exact UI changes

- Removed the small `MCQ Assembly Studio` subtitle and the top-right `Database-first demo / No LLM needed` pill. In the uploaded source there was no separate header `Home` link; the SecurePaper logo remains clickable as a home shortcut.
- Removed the home-page `Resume last session` banner and `How selection works` info block; removed the global prototype warning. The session retrieval API and underlying client-side resume handler are retained, although the visible resume shortcut was removed as requested.
- Removed the selection-strategy copy shown in the active exam heading, leaving the student name and question count.
- Removed the `Demo` wording from Sessions, and the entire `Demo boundaries` panel in How it works. The remaining workflow card uses the available width (no empty column).
- Removed the admin login instructions about setting the key for hosting, and replaced its `demo key` wording with `admin key`.
- Removed `demo` from the page's HTML description metadata. Existing colors, typography, spacing rules, navigation, forms and button behaviors remain as before.

## Verification

- Run `python -m pytest -q tests/` for backend API and UI-copy assertions.
- `node --check frontend/app.js` validates the JavaScript syntax.
- Updated local UI screenshots are saved under `docs/screenshots/` and include desktop and mobile views.
- Browser smoke checks verified the home page, paper selection (four options), answer saving, submission, result review, admin login, create/archive/restore question, Sessions and How it works using the real FastAPI API with an isolated test database. No JS exceptions were observed.

## Important storage note

The archive includes the original 90-question starter database for initial deployment. On a Render service without a persistent disk, a new deploy can reset the SQLite database and remove student sessions and added questions. Back up the live DB before updating, and mount the existing persistent volume (if any) at `SECUREPAPER_DATA_DIR` to preserve your data.
