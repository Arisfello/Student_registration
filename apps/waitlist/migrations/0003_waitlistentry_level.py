# Generated by Django 3.2.6 on 2021-09-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0002_alter_waitlistentry_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Class Level'),
        ),
    ]
