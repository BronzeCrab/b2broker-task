from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=36, decimal_places=18, default=0)

    def __str__(self):
        return f"Wallet_{self.label}_id={self.id}"


class Transaction(models.Model):
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Transaction_{self.txid}_id={self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.wallet:
            self.wallet.balance = sum(
                tr.amount for tr in self.wallet.transaction_set.all()
            )
            self.wallet.save()
