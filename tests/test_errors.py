import unittest

from tests.base import BaseTestCase


class TestErrors(BaseTestCase):
    def test_not_found(self):
        response = self.client.get('/some-unknown-url')
        self.assertEqual(response.status_code, 404)
        self.assertIn('File not Found', response.data.decode())


if __name__ == '__main__':
    unittest.main(verbosity=2)
