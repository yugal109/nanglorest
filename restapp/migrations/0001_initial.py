# Generated by Django 4.2.1 on 2023-05-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('image', models.ImageField(upload_to='menu/')),
                ('type', models.CharField(choices=[('starters', 'starters'), ('main_dishes', 'main_dishes'), ('deserts', 'deserts'), ('drinks', 'drinks')], default='starters', max_length=20)),
            ],
        ),
    ]
