# Generated by Django 3.2 on 2021-05-05 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_user_profileing_c_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profileing',
            old_name='image',
            new_name='embeddings',
        ),
    ]
