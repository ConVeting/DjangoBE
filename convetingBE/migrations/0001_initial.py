# Generated by Django 4.2.14 on 2024-08-13 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('symptom', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='SymptomDescription',
            fields=[
                ('seq', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=30)),
                ('pet', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'symptomdescription',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('seq', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='convetingBE.symptomdescription')),
                ('skin1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('skin7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye3', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye4', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye7', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye8', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye9', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye10', models.DecimalField(decimal_places=2, max_digits=5)),
                ('eye11', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'prediction',
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='convetingBE.disease')),
                ('seq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convetingBE.symptomdescription')),
            ],
            options={
                'db_table': 'diagnosis',
                'unique_together': {('seq', 'disease')},
            },
        ),
    ]
