# Generated by Django 3.0.2 on 2020-11-24 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='color',
            new_name='backgroundColor',
        ),
        migrations.AddField(
            model_name='style',
            name='fontColor',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='style',
            name='fontSize',
            field=models.IntegerField(),
        ),
    ]