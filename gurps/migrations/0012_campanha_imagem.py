# Generated by Django 5.1.2 on 2024-11-13 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurps', '0011_alter_campanha_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanha',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='global/img/campanhas/'),
        ),
    ]