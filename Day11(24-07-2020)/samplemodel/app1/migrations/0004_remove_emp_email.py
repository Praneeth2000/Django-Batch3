# Generated by Django 3.0.7 on 2020-07-23 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_emp_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='email',
        ),
    ]
