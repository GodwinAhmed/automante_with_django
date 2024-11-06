# Generated by Django 5.1.2 on 2024-10-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_alter_student_roll_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
