# Generated by Django 4.2 on 2023-04-29 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='status',
            new_name='is_deleted',
        ),
    ]
