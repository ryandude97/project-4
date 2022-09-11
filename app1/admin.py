from django.contrib import admin
from .models import Account, Transactions

class AccountAdministrator(admin.ModelAdmin):
    list_display = ('user', 'usd_balance', 'bitcoin_balance')

admin.site.register(Account, AccountAdministrator)

admin.site.register(Transactions)



