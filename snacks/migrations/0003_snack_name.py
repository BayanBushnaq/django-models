# Generated by Django 4.1.3 on 2022-11-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_alter_snack_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='name',
            field=models.CharField(default='snack', help_text='snack name', max_length=64),
        ),
    ]
