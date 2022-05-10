# Generated by Django 3.1.14 on 2022-04-12 03:45

from django.db import migrations, models


def create_internal_platform(apps, schema_editor):
    model = apps.get_model("assets", "Platform")
    db_alias = schema_editor.connection.alias
    type_platforms = (
        ('AIX', 'Unix', None),
    )
    for name, base, meta in type_platforms:
        defaults = {'name': name, 'base': base, 'meta': meta, 'internal': True}
        model.objects.using(db_alias).update_or_create(
            name=name, defaults=defaults
        )
        migrations.RunPython(create_internal_platform)


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0089_auto_20220310_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='number',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Asset number'),
        ),
        migrations.RunPython(create_internal_platform)
    ]