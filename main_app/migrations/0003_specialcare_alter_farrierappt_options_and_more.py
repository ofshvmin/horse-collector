# Generated by Django 4.2.16 on 2024-09-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_farrierappt'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialCare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('D', 'Diet'), ('E', 'Exercise'), ('M', 'Medical')], default='D', max_length=1)),
                ('frequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Q', 'Quarterly')], default='D', max_length=1)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='farrierappt',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='farrierappt',
            name='date',
            field=models.DateField(verbose_name='Appointment Date'),
        ),
    ]
