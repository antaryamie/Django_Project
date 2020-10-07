# Generated by Django 3.1.2 on 2020-10-07 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='login',
            options={'verbose_name_plural': 'login'},
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.python')),
            ],
        ),
    ]
