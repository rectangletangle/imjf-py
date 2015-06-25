
import unittest

from .client import ismyjsfucked
from .exceptions import IMJFException

class TestIntegration(unittest.TestCase):
    def url(self, test_name):
        return 'http://www.ismyjsfucked.com/tests/{name}.html'.format(name=test_name)

    def test_ok(self):
        assert ismyjsfucked(self.url('ok')) is False

    def test_exception(self):
        assert ismyjsfucked(self.url('exception')) is True

    def test_syntax_error(self):
        assert ismyjsfucked(self.url('syntax-error')) is True

    def test_unknown(self):
        assert ismyjsfucked(self.url('timeout')) is None

    def test_precedence(self):
        assert ismyjsfucked([self.url('ok'), self.url('syntax-error'), self.url('timeout')]) is True
        assert ismyjsfucked([self.url('ok'), self.url('syntax-error')]) is True
        assert ismyjsfucked([self.url('ok'), self.url('timeout')]) is None

    def test_invalid_url(self):
        with self.assertRaises(IMJFException) as context:
            ismyjsfucked('not-a-valid-url')

        assert str(context.exception) == "Invalid URL 'not-a-valid-url'"
