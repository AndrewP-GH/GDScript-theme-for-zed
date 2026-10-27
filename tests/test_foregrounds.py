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

if __name__ == "__main__":
    unittest.main()
