# Generated by Django 4.2.16 on 2024-09-10 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarrierAppt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service', models.CharField(choices=[('T', 'A Hoof Trim'), ('S', 'Shoes'), ('B', 'A Hoof Trim and Shoes')], default='T', max_length=1)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.horse')),
            ],
        ),
    ]
