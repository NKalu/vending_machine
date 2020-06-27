from src.vending_machine import VendingMachine
import unittest

class VendingMachineTest(unittest.TestCase):
    def setUp(self):
        self.vending_machine = VendingMachine()

    def test_vending_display(self):
        # amount with nothing selected
        self.assertEqual(self.vending_machine.vending_display(), "INSERT COIN")
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.assertEqual(self.vending_machine.vending_display(), "$0.25")

        # amount with selection
        self.vending_machine.product_select.select_product('chips')
        self.assertEqual(self.vending_machine.vending_display(), "PRICE $0.25")

        # thank you message after enough inserted
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.assertEqual(self.vending_machine.vending_display(), "THANK YOU")
        self.assertEqual(self.vending_machine.vending_display(), "INSERT COIN")


    def test_make_change(self):
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.vending_machine.product_select.select_product('chips')
        self.assertEqual(self.vending_machine.vending_display(), '')


    def test_sold_out(self):
        self.vending_machine.product_select.product_options = {
            'cola': (1, False),
            'chips': (.5, False),
            'candy': (.65, False)
        }

        # Test to see insert coin after sold out
        self.vending_machine.product_select.select_product('chips')
        self.assertEqual(self.vending_machine.vending_display(), "SOLD OUT")
        self.assertEqual(self.vending_machine.vending_display(), "INSERT COIN")

        # Test to see amount inserted after sold out
        self.vending_machine.coin_accept.accept_coins('quarter')
        self.vending_machine.product_select.select_product('chips')
        self.assertEqual(self.vending_machine.vending_display(), "SOLD OUT")
        self.assertEqual(self.vending_machine.vending_display(), "$0.25")


    def test_exact_change_only(self):
        self.vending_machine.change_in_machine = 0
        self.assertEqual(self.vending_machine.vending_display(), "EXACT CHANGE ONLY")
