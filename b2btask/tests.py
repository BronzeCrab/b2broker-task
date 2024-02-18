from django.test import Client, TestCase
from b2btask.models import Wallet, Transaction


class B2btaskTestCase(TestCase):

    def test_migrations_are_ok(self):
        """Проверяем как отрабатывает миграция.
        Создаются ли тестовые записи в бд."""
        wallets = Wallet.objects.all()
        transactions = Transaction.objects.all()
        assert len(wallets) > 0
        assert len(transactions) > 0
        for wallet in wallets:
            assert wallet.balance > 0
            balance = sum([tr.amount for tr in wallet.transaction_set.all()])
            assert wallet.balance == balance

    def test_wallet_balance_is_updated_after_transaction_creation(self):
        """После создания новой Транзакции, баланс в Кошельке должен
        соответственно обновиться."""
        wallet = Wallet.objects.first()
        assert wallet
        assert wallet.balance == 15
        new_tr = Transaction.objects.create(
            txid="testing", amount=150, wallet_id=wallet.id
        )
        assert new_tr
        assert new_tr.amount == 150
        assert new_tr.wallet_id == wallet.id

        wallet = Wallet.objects.get(id=wallet.id)
        assert wallet.balance == 15 + 150
