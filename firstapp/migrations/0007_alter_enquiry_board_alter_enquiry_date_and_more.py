# Generated by Django 4.2.7 on 2024-03-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='board',
            field=models.CharField(choices=[('1', 'CBSC'), ('2', 'ISCE'), ('3', 'SSC'), ('4', 'SEMI'), ('5', 'COLLEGE')], max_length=1),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='scltime',
            field=models.CharField(choices=[('1', 'Morning'), ('2', 'Afternoon')], max_length=1),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='std',
            field=models.CharField(choices=[('1', 'VII'), ('2', 'VIII'), ('3', 'IX'), ('4', 'X'), ('5', 'XI'), ('6', 'XII')], max_length=1),
        ),
    ]