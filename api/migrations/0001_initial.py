# Generated by Django 4.0.4 on 2022-06-14 02:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('corner_or_ave', models.CharField(max_length=100)),
                ('apto', models.CharField(max_length=100, verbose_name='No. Y/O APTO')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('district', models.PositiveIntegerField()),
                ('political_area', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('subordinate', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'core',
            },
        ),
        migrations.CreateModel(
            name='DeclarationDate',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'declaration_date',
            },
        ),
        migrations.CreateModel(
            name='Militant',
            fields=[
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('first_lastname', models.CharField(max_length=100)),
                ('second_lastname', models.CharField(max_length=100)),
                ('register_date', models.DateTimeField(default=datetime.datetime(2022, 6, 14, 2, 1, 9, 602199))),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.address')),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='militants', to='api.core')),
            ],
            options={
                'db_table': 'militant',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(choices=[('Excelente', 'Excelente'), ('Bien', 'Bien'), ('Majomeno', 'Majomeno'), ('Mal', 'Mal')], max_length=10)),
                ('militant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.militant')),
            ],
            options={
                'db_table': 'participant',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='PaymentDate',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'payment_date',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('orientation', models.TextField()),
                ('militants', models.ManyToManyField(through='api.Participant', to='api.militant')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='PaymentNorm',
            fields=[
                ('lower_limit', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('upper_limit', models.PositiveIntegerField()),
                ('percent', models.PositiveIntegerField(null=True)),
                ('amount_to_pay', models.PositiveIntegerField(null=True)),
            ],
            options={
                'db_table': 'payment_norm',
                'unique_together': {('lower_limit', 'upper_limit')},
            },
        ),
        migrations.CreateModel(
            name='PaymentDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('share', models.PositiveIntegerField()),
                ('declaration_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.declarationdate')),
                ('militant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_declaration', to='api.militant')),
                ('payment_date', models.ManyToManyField(through='api.Payment', to='api.paymentdate')),
                ('payment_norm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paymentnorm')),
            ],
            options={
                'db_table': 'payment_declaration',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paymentdate'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_declaration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paymentdeclaration'),
        ),
        migrations.AddField(
            model_name='participant',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task'),
        ),
        migrations.AddField(
            model_name='militant',
            name='declaration_date',
            field=models.ManyToManyField(through='api.PaymentDeclaration', to='api.declarationdate'),
        ),
        migrations.AlterUniqueTogether(
            name='payment',
            unique_together={('payment_declaration', 'payment_date')},
        ),
        migrations.AlterUniqueTogether(
            name='participant',
            unique_together={('militant', 'task')},
        ),
    ]
