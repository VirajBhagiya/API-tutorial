import pytest
from app.calculations import add, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3), 
    (3, 7, 10), 
    (5, 5, 10)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected


def test_bank_set_initial_balance():
    account = BankAccount(100)
    assert account.balance == 100
    
def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_deposit():
    bank_account = BankAccount(100)
    bank_account.deposit(100)
    assert bank_account.balance == 200
    
def test_bank_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50

def test_collect_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110