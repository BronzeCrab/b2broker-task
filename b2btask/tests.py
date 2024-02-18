from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from b2btask.models import Wallet, Transaction


class B2btaskTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="afoobar")
        token = Token.objects.create(user=user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_migrations_are_ok(self):
        """Проверяем как отрабатывает миграция.
        Создаются ли тестовые записи в бд. Баланс Кошельков
        должен биться с суммой Тразацкций."""
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

    def test_wallet_balance_is_updated_after_transaction_update(self):
        """После обновления какой-то Транзакции, баланс в Кошельке должен
        соответственно обновиться."""
        wallet = Wallet.objects.first()
        assert wallet
        assert wallet.balance == 15
        assert len(wallet.transaction_set.all()) > 0

        tr = Transaction.objects.filter(wallet_id=wallet.id).first()
        tr.amount += 5
        tr.save()

        wallet = Wallet.objects.get(id=wallet.id)
        assert wallet.balance == 15 + 5

    def test_get_all_wallets(self):
        resp = self.client.get("/wallets/")

        res = resp.json()["results"]
        amount_of_wallets = Wallet.objects.count()
        assert amount_of_wallets > 0
        assert len(res) == amount_of_wallets
