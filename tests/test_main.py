import unittest

from tests.base import BaseTestCase


class TestMain(BaseTestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('This is the home page of the ', response.data.decode())


if __name__ == '__main__':
    unittest.main(verbosity=2)
