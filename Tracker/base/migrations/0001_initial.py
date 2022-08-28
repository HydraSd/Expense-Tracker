# Generated by Django 4.0.5 on 2022-06-23 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('FD', 'Food'), ('ED', 'Education'), ('TR', 'Transport'), ('EN', 'Entertainment'), ('HE', 'Health'), ('CR', 'Credits'), ('OT', 'Other')], default='FD', max_length=2)),
                ('detail', models.TextField(blank=True, max_length=200)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
    ]
