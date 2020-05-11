from django.db import models
from .classmodel import MarriageClass
from .marriagemodel import MarriageBasic
from django.utils.html import format_html
class MarriageTuition(models.Model):
    class Meta:
        verbose_name = '婚姻指导交费信息'
        verbose_name_plural = verbose_name

    relate_class = models.ForeignKey(MarriageClass, on_delete=models.CASCADE, verbose_name='班级',null=True,blank=True)
    relate_marriage = models.OneToOneField(MarriageBasic, on_delete=models.CASCADE, verbose_name='学号', primary_key=True)
    fee_train = models.CharField(max_length=128, verbose_name='培训费', blank=True, null=True,default='空')
    fee_material = models.CharField(max_length=128, verbose_name='教材费', blank=True, null=True,default='空')
    fee_exam = models.CharField(max_length=128, verbose_name='考试费', blank=True, null=True,default='空')
    fee_total = models.CharField(max_length=128, verbose_name='总费用', blank=True, null=True,default='空')
    fee_date = models.CharField(max_length=128,verbose_name='缴费日期', blank=True, null=True,default='空')
    fee_method = models.CharField(max_length=128, verbose_name='缴费方式', blank=True, null=True,default='空')
    fee_tax = models.CharField(max_length=128,verbose_name='发票号',blank=True,null=True,default='空')
    fee_invoice_header = models.CharField(max_length=128, verbose_name='发票抬头', blank=True, null=True, default='空')
    fee_invoice_id = models.CharField(max_length=128, verbose_name='发票机构代码', blank=True, null=True, default='空')
    fee_invoice_date = models.CharField(max_length=128, verbose_name='发票开票日期', blank=True, null=True, default='空')
    fee_other = models.TextField(verbose_name='备注',blank=True,null=True,default='空')

    # TODO CODEREVICEW:模型的三种继承方式和自定义方法
    def get_mar_name(self):
        info = self.relate_marriage.mar_name
        if self.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'

        return format_html('<span style="color:{};">{}</span>', color_code, info)

    get_mar_name.short_description = u'姓名'
    get_mar_name.allow_tags = get_mar_name.is_column = True

    def get_mar_class(self):
        return self.relate_marriage.mar_class.class_name

    get_mar_class.short_description = u'班级'
    get_mar_class.allow_tags = get_mar_name.is_column = True

    def get_mar_num(self):
        return self.relate_marriage.mar_number

    get_mar_num.short_description = '学号'
    get_mar_num.allow_tags = get_mar_num.is_colume = True

    def __str__(self):
        return str(self.relate_marriage.mar_name)
