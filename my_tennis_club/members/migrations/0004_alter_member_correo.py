# Generated by Django 5.1 on 2024-08-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='correo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
