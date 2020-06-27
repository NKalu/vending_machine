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

    def test_return_to_customer(self):
        self.coin_accept.accept_coins('quarter')
        self.coin_accept.accept_coins('quarter')
        self.coin_accept.accept_coins('dime')
        self.coin_accept.accept_coins('nickel')
        self.assertEqual(self.coin_accept.return_coins_to_customer(), "quarter sent to Coin Return\nquarter sent to Coin Return"
                                                                      "\ndime sent to Coin Return\nnickel sent to Coin Return")
        

    def test_accept_coin(self):
        self.coin_accept.accept_coins('quarter')
        self.assertEqual(self.coin_accept.coin_value, .25)
        self.coin_accept.accept_coins('penny')
        self.assertEqual(self.coin_accept.coin_value, .25)
        self.coin_accept.accept_coins('golden dollar')
        self.assertEqual(self.coin_accept.coin_value, .25)
        self.coin_accept.accept_coins('dime')
        self.assertEqual(self.coin_accept.coin_value, .35)

if __name__ == '__main__':
    unittest.main()
