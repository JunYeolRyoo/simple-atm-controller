import unittest
from simple_atm_controller import Account, ATM

class TestATM(unittest.TestCase):

    def test_account_creation(self):
        account1 = Account.create_account(123456, 1234, 500)
        self.assertEqual(account1.get_balance(), 500)

    def test_duplicate_account_creation(self):
        with self.assertRaises(ValueError):
            Account.create_account(123456, 4321, 1000)

    def test_deposit(self):
        atm = ATM()
        account1 = Account.create_account(111111, 0000, 300)
        atm.add_account(account1)
        atm.insert_card(111111)
        atm.enter_pin(0000)
        atm.deposit(200)
        self.assertEqual(account1.get_balance(), 500)

    def test_deposit_zero_amount(self):
        atm = ATM()
        account1 = Account.create_account(211111,0000,400)
        atm.add_account(account1)
        atm.insert_card(211111)
        atm.enter_pin(400)
        self.assertEqual(account1.deposit(0),False)

    def test_withdraw(self):
        atm = ATM()
        account1 = Account.create_account(111112, 1111, 400)
        atm.add_account(account1)
        atm.insert_card(111112)
        atm.enter_pin(1111)
        atm.withdraw(100)
        self.assertEqual(account1.get_balance(), 300)
     
    def test_withdraw_exceeds_balance(self):
        atm = ATM()
        account1 = Account.create_account(111114, 1010, 100)
        atm.add_account(account1)
        atm.insert_card(111114)
        atm.enter_pin(1010)
        result = atm.withdraw(200)
        self.assertFalse(result)
        self.assertEqual(account1.get_balance(), 100)

    def test_pin_verification_failure(self):
        atm = ATM()
        account1 = Account.create_account(111115, 1111, 600)
        atm.add_account(account1)
        atm.insert_card(111115)
        result = atm.enter_pin(9999)
        self.assertFalse(result)

    def test_eject_card(self):
        atm = ATM()
        account1 = Account.create_account(111116, 1212, 700)
        atm.add_account(account1)
        atm.insert_card(111116)
        atm.enter_pin(1212)
        atm.eject_card()
        self.assertIsNone(atm.current_account)

if __name__ == '__main__':
    unittest.main()