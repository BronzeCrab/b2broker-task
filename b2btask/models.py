from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=36, decimal_places=18)


class Transaction(models.Model):
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True)
