# Generated by Django 2.2.5 on 2019-10-25 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20191024_1325'),
        ('teacher', '0002_auto_20191019_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '心理教师授课信息', 'verbose_name_plural': '心理教师授课信息'},
        ),
        migrations.CreateModel(
            name='FamilyTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=128, verbose_name='上课教师')),
                ('teacher_info', models.CharField(max_length=256, verbose_name='上课内容')),
                ('teacher_date', models.DateField(verbose_name='上课时间')),
                ('teacher_fare', models.CharField(max_length=128, verbose_name='课时费用')),
                ('teacher_paid', models.CharField(choices=[('是', '是'), ('否', '否')], max_length=16, verbose_name='课时费是否已支付')),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentClass', verbose_name='教师上课班级')),
            ],
            options={
                'verbose_name': '家庭教师授课信息',
                'verbose_name_plural': '家庭教师授课信息',
            },
        ),
    ]