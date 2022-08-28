# Generated by Django 4.0.5 on 2022-07-12 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True, verbose_name='Date of Payment')),
                ('file', models.ImageField(null=True, upload_to='')),
                ('amount', models.FloatField(default=())),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.classes')),
            ],
        ),
    ]