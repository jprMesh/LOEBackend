# Generated by Django 3.1.7 on 2021-07-23 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0011_teamratinghistory_squashed_0013_teamratinghistory_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamratinghistory',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ratings.match'),
        ),
    ]
