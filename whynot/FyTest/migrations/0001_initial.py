# Generated by Django 2.2.1 on 2019-05-23 09:28

from django.db import migrations, models
import fysom


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=128)),
            ],
            bases=(fysom.FysomGlobalMixin, models.Model),
        ),
    ]
