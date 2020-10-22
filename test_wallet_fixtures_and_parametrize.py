import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def wallet_0():
    '''return wallet with zero balance'''
    return Wallet()

@pytest.mark.parametrize("earned,spent,expected", [
    (30,10,20),
    (20,2,18),
    (1000,0,1000),
])

def test_transactions(wallet_0,earned,spent,expected):
    wallet_0.add_cash(earned)
    wallet_0.spend_cash(spent)
    assert wallet_0.balance == expected