from django.contrib import admin
from home.models import Complain
from home.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class ShankarUserAdmin(UserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, ShankarUserAdmin)
admin.site.register(Complain)
