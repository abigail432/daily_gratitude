# Generated by Django 4.0.2 on 2022-02-05 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daily_grat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graditude',
            name='user_submitted',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='daily_grat.user'),
        ),
    ]
