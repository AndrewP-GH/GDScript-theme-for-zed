import json
import unittest
from pathlib import Path

THEME_PATH = Path(__file__).resolve().parents[1] / "themes" / "gdscript.json"
THEMES = json.loads(THEME_PATH.read_text())["themes"]

class ForegroundTests(unittest.TestCase):
    def test_markdown_preview_inherits_vscode_editor_foreground(self):
        for theme in THEMES:
            with self.subTest(theme=theme["name"]):
                self.assertEqual(theme["style"]["text"].upper(), "#EEFFFF")

    def test_unselected_project_labels_inherit_opaque_vscode_ui_foreground(self):
        for theme in THEMES:
            with self.subTest(theme=theme["name"]):
                self.assertEqual(theme["style"]["text.muted"].upper(), "#CCCCCC")

    def test_preview_selection_matches_reference_without_changing_editor_selection(self):
        for theme in THEMES:
            with self.subTest(theme=theme["name"]):
                self.assertEqual(theme["style"].get("element.selection_background"), "#5C84B2")
                self.assertEqual(theme["style"]["players"][0]["selection"].upper(), "#264F78")

    def test_default_ansi_cells_match_the_terminal_background(self):
        for theme in THEMES:
            with self.subTest(theme=theme["name"]):
                self.assertEqual(theme["style"].get("terminal.ansi.background"), "#202531")

    def test_preview_links_use_vscode_link_foreground(self):
        for theme in THEMES:
            with self.subTest(theme=theme["name"]):
                self.assertEqual(theme["style"]["text.accent"].upper(), "#3794FF")

    def test_search_results_use_vscode_match_highlights(self):
        for theme in THEMES:
            for role, color in {
                "search.match_background": "#EA5C0055",
                "search.active_match_background": "#515C6A",
            }.items():
                with self.subTest(theme=theme["name"], role=role):
                    self.assertEqual(theme["style"].get(role), color)

if __name__ == "__main__":
    unittest.main()
