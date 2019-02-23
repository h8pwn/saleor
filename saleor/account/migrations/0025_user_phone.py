# Generated by Django 2.1.5 on 2019-02-20 13:59

from django.db import migrations, models
import saleor.account.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20181011_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[saleor.account.validators.validate_possible_number]),
        ),
    ]