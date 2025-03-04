# Generated by Django 5.1.5 on 2025-02-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DefectsPortal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefectsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_id', models.CharField(max_length=100)),
                ('defect_name', models.CharField(max_length=100)),
                ('defect_type', models.CharField(max_length=100)),
                ('assigned_by', models.CharField(max_length=100)),
                ('assigned_to', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Defect',
        ),
    ]
