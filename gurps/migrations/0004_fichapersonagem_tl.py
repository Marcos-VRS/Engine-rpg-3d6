# Generated by Django 5.1.2 on 2024-11-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurps', '0003_delete_camapnhas'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichapersonagem',
            name='tl',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
