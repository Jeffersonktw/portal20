# Generated by Django 3.2.5 on 2021-09-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0066_alter_datasetorganization_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='organization_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='status',
            field=models.CharField(choices=[('PUBLIC', '公開'), ('PRIVATE', '非公開')], max_length=10, verbose_name='status'),
        ),
    ]
