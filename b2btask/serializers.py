from b2btask.models import Wallet, Transaction
from rest_framework import serializers


class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = ["label", "balance"]


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ["txid", "amount", "wallet"]
