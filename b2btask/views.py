from rest_framework import permissions, viewsets

from b2btask.models import Wallet, Transaction
from b2btask.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows wallets to be viewed or edited.
    """

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("label", "balance")


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transactions to be viewed or edited.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ("txid", "amount", "wallet")
