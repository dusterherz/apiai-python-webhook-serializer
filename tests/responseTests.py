import unittest
from apiaiWebhookSerializer import Response

class TestReponse(unittest.TestCase):
    speech = "I love cupcake"
    displayText = "Cupcake ipsum dolor sit amet jelly-o danish marshmallow oat cake. \
                Oat cake caramels caramels croissant topping icing carrot cake. \
                Gingerbread fruitcake biscuit sesame snaps chocolate bar."
    source = "test"
    response = Response(speech, displayText, source)

    def test_init(self):
        self.assertEqual(self.response.speech, self.speech)
        self.assertEqual(self.response.source, self.source)
        self.assertEqual(self.response.displayText, self.displayText)
        self.assertNotEqual(self.response.source, "notTest")

    def test_format(self):
        test = {"speech": self.speech, "displayText": self.displayText, "source": self.source}
        self.assertEqual(self.response.format(), test)

if __name__ == '__main__':
    unittest.main()
