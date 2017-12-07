"""
This script is used to periodically clear the database in the Saleor demo app.
The script is copied to the proper location which makes it accessible for
`python manage.py` command.
"""

from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from saleor.cart.models import Cart
from saleor.discount.models import Sale, Voucher
from saleor.order.models import Order, Payment
from saleor.product.models import Product
from saleor.shipping.models import ShippingMethod
from saleor.userprofile.models import User


class Command(BaseCommand):
    help = 'Clear database preserving staff accounts and configuration'

    def handle(self, *args, **kwargs):
        Cart.objects.all().delete()
        self.stdout.write('Removed carts')

        Payment.objects.all().delete()
        self.stdout.write('Removed payments')

        Order.objects.all().delete()
        self.stdout.write('Removed orders')

        Product.objects.all().delete()
        self.stdout.write('Removed products')

        Sale.objects.all().delete()
        self.stdout.write('Removed sales')

        ShippingMethod.objects.all().delete()
        self.stdout.write('Removed shipping methods')

        Voucher.objects.all().delete()
        self.stdout.write('Removed vouchers')

        # Delete all users except for staff members.
        staff = User.objects.filter(is_staff=True)
        User.objects.exclude(pk__in=staff).delete()
        self.stdout.write('Removed customers')

        # Remove addresses of staff members.
        for user in staff:
            user.addresses.all().delete()
        self.stdout.write('Removed staff addresses')
