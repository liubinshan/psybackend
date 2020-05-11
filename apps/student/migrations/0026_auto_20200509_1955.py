# Generated by Django 2.2.5 on 2020-05-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_auto_20200327_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentbasic',
            name='stu_group',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='组别与职务'),
        ),
        migrations.AddField(
            model_name='studentbasic',
            name='stu_type',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='学员类型'),
        ),
        migrations.AddField(
            model_name='studenttextbook',
            name='text_CAS',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='中科院资料'),
        ),
        migrations.AddField(
            model_name='studenttextbook',
            name='text_guide',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='培训指南'),
        ),
        migrations.AddField(
            model_name='tuition',
            name='fee_info',
            field=models.TextField(blank=True, default='空', max_length=128, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='tuition',
            name='fee_invoice_inc',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='出票单位'),
        ),
        migrations.AlterField(
            model_name='studenttextbook',
            name='text_basic',
            field=models.CharField(blank=True, default='空', max_length=128, null=True, verbose_name='基础知识'),
        ),
    ]
