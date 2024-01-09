# Generated by Django 4.2.6 on 2023-12-27 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('inst_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sname', models.CharField(max_length=20)),
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('smob', models.IntegerField()),
                ('sfee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('tname', models.CharField(max_length=20)),
                ('tid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('inst_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.institute')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainer')),
            ],
        ),
    ]
