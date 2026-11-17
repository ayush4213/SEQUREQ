"""Regression checks for requested nonfunctional UI copy/layout cleanup."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_cleaned_ui_excludes_removed_text_and_sections():
    script = (ROOT / 'frontend/app.js').read_text(encoding='utf-8')
    html = (ROOT / 'frontend/index.html').read_text(encoding='utf-8')
    removed_copy = (
        'MCQ Assembly Studio', 'Database-first demo', 'No LLM needed',
        'Resume last session', 'How selection works:', 'Prototype only',
        'Demo history', 'Demo boundaries', 'Selection, not generation.',
        'No CDN', 'For hosting, set', 'shared demo key',
        'session.blueprint.strategy',
    )
    for snippet in removed_copy:
        assert snippet not in script
    assert 'demo MCQ exam assembly' not in html


def test_existing_client_flows_and_data_actions_remain_present():
    script = (ROOT / 'frontend/app.js').read_text(encoding='utf-8')
    for snippet in (
        "['create','Create exam']", "['admin','Question bank']",
        "['sessions','Sessions']", "['about','How it works']",
        "data-action=\"start\"", "data-action=\"submit\"",
        "data-action=\"answer\"", "data-action=\"goto\"",
        "id=\"admin-login\"", "id=\"add-question\"",
        "data-action=\"toggle\"", "id=\"import-file\"",
        "data-action=\"refresh-sessions\"",
        "if(a==='resume')", "getLast()", "setLast(data.id)",
        "api('/sessions/'", "function renderAbout()",
    ):
        assert snippet in script
