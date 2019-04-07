# Generated by Django 2.2 on 2019-04-06 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0004_auto_20190406_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcartitem',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='数量'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='ユーザ'),
        ),
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='amazon.ShoppingCart', verbose_name='ショッピングカート'),
        ),
    ]