from src.vending_machine import VendingMachine
import unittest

class VendingMachineTest(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_vending_display(self):
        self.assertEqual(self.vending_machine.vending_display(), "INSERT COIN")
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.assertEqual(self.vending_machine.vending_display(), "$0.25")
        self.vending_machine.product_select.select_product('chips')
        self.assertEqual(self.vending_machine.vending_display(), "PRICE $0.25")
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.assertEqual(self.vending_machine.vending_display(), "THANK YOU")
        self.assertEqual(self.vending_machine.vending_display(), "INSERT COIN")

