from src.vending_features.coin_accept import CoinAcceptor
import unittest

class CoinAcceptorTest(unittest.TestCase):
    def setUp(self):
        self.coin_accept = CoinAcceptor()

    def test_weigh_coin(self):
        self.assertEqual(self.coin_accept.weigh_coin('dime'), 'deim')
        self.assertEqual(self.coin_accept.weigh_coin('penny'), 'ennpy')
        self.assertEqual(self.coin_accept.weigh_coin('nickel'), 'ceikln')
        self.assertEqual(self.coin_accept.weigh_coin('quarter'), 'aeqrrtu')

    def test_coin_display(self):
        self.assertEqual(self.coin_accept.coin_display(), 'Insert Coin')
        self.coin_accept.accept_coins('nickel')
        self.assertEqual(self.coin_accept.coin_display(), '5')

    def test_accept_coin(self):
        self.coin_accept.accept_coins('quarter')
        self.assertEqual(self.coin_accept.coin_value, 25)
        self.coin_accept.accept_coins('penny')
        self.assertEqual(self.coin_accept.coin_value, 25)
        self.coin_accept.accept_coins('golden dollar')
        self.assertEqual(self.coin_accept.coin_value, 25)
        self.coin_accept.accept_coins('dime')
        self.assertEqual(self.coin_accept.coin_value, 35)

if __name__ == '__main__':
    unittest.main()
