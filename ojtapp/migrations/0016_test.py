# Generated by Django 2.2.3 on 2019-07-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojtapp', '0015_select_switch_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_text', models.CharField(max_length=100)),
            ],
        ),
    ]
