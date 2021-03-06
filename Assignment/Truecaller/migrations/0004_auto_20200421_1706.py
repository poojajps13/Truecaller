# Generated by Django 2.1.8 on 2020-04-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truecaller', '0003_auto_20200420_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
