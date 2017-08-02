import unittest
from apiaiWebhookSerializer import Request


class requestTest(unittest.TestCase):
    f = open('tests/request.json', 'r')
    body = f.read()

    def test_format(self):
        request = Request(self.body)
        v = request.__dict__
        print(v)
        self.assertEqual(request.lang, "en")
        self.assertEqual(request.result.parameters.city, "Rome")
        self.assertEqual(request.result.score, 1.0)
        self.assertEqual(request.originalRequest.source, "google")
        self.assertEqual(request.timestamp, "2017-02-09T16:06:01.908Z")


if __name__ == '__main__':
    unittest.main()
