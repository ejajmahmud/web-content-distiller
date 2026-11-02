"""Unit tests for WebContentDistiller."""
import unittest
from web_content_distiller.distiller import distill_html

class TestWebDistiller(unittest.TestCase):
    def test_distill(self):
        html = "<script>alert('x')</script><h1>Breaking News</h1><p>Story paragraph.</p>"
        res = distill_html(html)
        self.assertNotIn("alert", res)
        self.assertIn("# Breaking News", res)
        self.assertIn("Story paragraph.", res)

if __name__ == "__main__":
    unittest.main()
