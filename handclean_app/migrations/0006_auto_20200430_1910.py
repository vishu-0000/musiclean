# Generated by Django 2.1 on 2020-04-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handclean_app', '0005_auto_20200415_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='picture',
            field=models.CharField(default='https://res.cloudinary.com/do8xzkgcs/image/upload/v1571618470/gbvmr9fwrwcz9xp0ycos.png', max_length=1000),
        ),
    ]
