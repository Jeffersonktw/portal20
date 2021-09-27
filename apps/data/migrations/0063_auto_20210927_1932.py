# Generated by Django 3.2.5 on 2021-09-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0062_alter_taxon_name_zh'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxon',
            options={'ordering': ['id', 'name']},
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='administrative_contact',
            field=models.CharField(default='', max_length=256, verbose_name='administrative_contact'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='country_or_area',
            field=models.CharField(default='', max_length=256, verbose_name='country_or_area'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='dataset_num',
            field=models.IntegerField(default=0, null=True, verbose_name='dataset_num'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='endorsed_by',
            field=models.CharField(default='', max_length=256, verbose_name='endorsed_by'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='installations',
            field=models.CharField(default='', max_length=256, verbose_name='installations'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='occurences_num',
            field=models.IntegerField(default=0, null=True, verbose_name='country_or_area'),
        ),
        migrations.AddField(
            model_name='datasetorganization',
            name='technical_contact',
            field=models.CharField(default='', max_length=256, verbose_name='technical_contact'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dwc_core_type',
            field=models.CharField(choices=[('Occurrence', '出現紀錄'), ('checklist', '物種名錄'), ('Sampling event', '調查活動')], max_length=128, null=True, verbose_name='Dw-C Core Type'),
        ),
    ]
