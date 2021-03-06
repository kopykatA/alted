# Generated by Django 2.0 on 2018-04-26 09:52

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0002_auto_20180423_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='target_type',
            field=models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'markets'), ('model', 'market'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'coins'), ('model', 'coin'), _connector='AND'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
