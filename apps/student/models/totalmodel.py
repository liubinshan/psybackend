from django.db import models
from .studentmodel import StudentBasic
from .classmodel import StudentClass
from .exammodel import StudentExam
from .examextramodel import StudentExamExtra
from .ondutymodel import Onduty
from .tuitionmodel import Tuition
from .wechatmodel import StudentWechat
from django.utils.html import format_html
class Total(models.Model):
    class Meta:
        verbose_name="心理学员招生信息总览"
        verbose_name_plural = verbose_name
    student = models.OneToOneField(StudentBasic,on_delete=models.CASCADE,verbose_name="学生")
    # tuition = models.OneToOneField(Tuition,on_delete=models.CASCADE,verbose_name="财务信息",null=True,blank=True)

    def __str__(self):
        return str(self.student.stu_number)+"-"+str(self.student.stu_name)

    def stu_number(self):
        return self.student.stu_number

    stu_number.short_description = "学号"

    def stu_type(self):
        return self.student.stu_type

    stu_type.short_description = "学员类型"

    def stu_group(self):
        return self.student.stu_group

    stu_group.short_description = "组别与职务"


    def stu_name(self):
        info = self.student.stu_name
        if self.student.tuition.fee_date == '空':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html('<span style="color:{};">{}</span>', color_code, info)

    stu_name.short_description = "姓名"

    def stu_gender(self):
        return self.student.stu_gender

    stu_gender.short_description = "年龄"

    def stu_class(self):
        return self.student.stu_class

    stu_class.short_description = "班级"

    def stu_class_num(self):
        return self.student.stu_class_num

    stu_class_num.short_description = "班级序号"

    def stu_level(self):
        return self.student.stu_level

    stu_level.short_description = "级别"

    def stu_id_number(self):
        return self.student.stu_id_number

    stu_id_number.short_description = "身份证号"

    def stu_loc(self):
        return self.student.stu_loc

    stu_loc.short_description = "所在地"

    def stu_deg(self):
        return self.student.stu_deg

    stu_deg.short_description = "学历"

    def stu_major(self):
        return self.student.stu_major

    stu_major.short_description = "专业"

    def stu_company(self):
        return self.student.stu_company

    stu_company.short_description = "工作单位"

    def stu_duty(self):
        return self.student.stu_duty

    stu_duty.short_description = "职务"

    def stu_status(self):
        return self.student.stu_status

    stu_status.short_description = "职称"

    def stu_origin(self):
        return self.student.stu_origin

    stu_origin.short_description = "生源来源"

    def stu_cellphone(self):
        return self.student.stu_cellphone

    stu_cellphone.short_description = "手机号"

    def stu_wechat(self):
        return self.student.stu_wechat

    stu_wechat.short_description = "微信"

    def stu_qq(self):
        return self.student.stu_qq

    stu_qq.short_description = "qq"

    def stu_signup_date(self):
        return self.student.stu_signup_date

    stu_signup_date.short_description = "报名日期"

    def stu_signup_people(self):
        return self.student.stu_signup_people

    stu_signup_people.short_description = "具体招生人"

    def stu_other(self):
        return self.student.stu_other

    stu_other.short_description = "备注"

    def fee_train(self):
        return self.student.tuition.fee_train

    fee_train.short_description = "培训费"

    def fee_material(self):
        return self.student.tuition.fee_material

    fee_material.short_description = "教材费"

    def fee_exam(self):
        return self.student.tuition.fee_exam

    fee_exam.short_description = "考试费"

    def fee_total(self):
        return self.student.tuition.fee_total

    fee_total.short_description = "总费用"

    # def fee_exam_extra(self):
    #     return self.student.tuition.fee_exam_extra
    #
    # fee_exam_extra.short_description = "补考费"

    def fee_date(self):
        return self.student.tuition.fee_date

    fee_date.short_description = "缴费日期"

    def fee_method(self):
        return self.student.tuition.fee_method

    fee_method.short_description = "缴费方式"

    def fee_id(self):
        return self.student.tuition.fee_id

    fee_id.short_description = "收据号"

    def fee_tax(self):
        return self.student.tuition.fee_tax

    fee_tax.short_description = "发票号"

    def fee_invoice_header(self):
        return self.student.tuition.fee_invoice_header

    fee_invoice_header.short_description = "发票抬头"

    def fee_invoice_id(self):
        return self.student.tuition.fee_invoice_id

    fee_invoice_id.short_description = "发票机构代码"

    def fee_invoice_date(self):
        return self.student.tuition.fee_invoice_date

    fee_invoice_date.short_description = "发票开票日期"

    def fee_invoice_inc(self):
        return self.student.tuition.fee_invoice_inc

    fee_invoice_inc.short_description = "出票单位"

    def fee_info(self):
        return self.student.tuition.fee_info

    fee_info.short_description = "备注"

    def text_basic(self):
        return self.student.studenttextbook.text_basic

    text_basic.short_description = "基础技能"

    def text_sec(self):
        return self.student.studenttextbook.text_sec

    text_sec.short_description = "二级技能"

    def text_sec_exer(self):
        return self.student.studenttextbook.text_sec_exer

    text_sec_exer.short_description = "二级习题"

    def text_sec_measure(self):
        return self.student.studenttextbook.text_sec_measure

    text_sec_measure.short_description = "二级量表"

    def text_thr(self):
        return self.student.studenttextbook.text_thr

    text_thr.short_description = "三级技能"

    def text_thr_exer(self):
        return self.student.studenttextbook.text_thr_exer

    text_thr_exer.short_description = "三级习题"

    def text_thr_measure(self):
        return self.student.studenttextbook.text_thr_measure

    text_thr_measure.short_description = "三级量表"

    def text_manual(self):
        return self.student.studenttextbook.text_manual

    text_manual.short_description = "学员手册"

    def text_exam(self):
        return self.student.studenttextbook.text_exam

    text_exam.short_description = "模拟试卷"

    def text_CAS(self):
        return self.student.studenttextbook.text_CAS

    text_CAS.short_description = "中科院资料"

    def text_guide(self):
        return self.student.studenttextbook.text_guide

    text_guide.short_description = "培训指南"

    def text_other(self):
        return self.student.studenttextbook.text_other

    text_other.short_description = "备注"

    def wechat_number(self):
        return self.student.studentwechat.wechat_number

    wechat_number.short_description = "平台绑定号码"

    def wechat_nickname(self):
        return self.student.studentwechat.wechat_nickname

    wechat_nickname.short_description = "微信昵称"

    def wechat_date(self):
        return self.student.studentwechat.wechat_date

    wechat_date.short_description = "开通日期"

    def wechat_test(self):
        return self.student.studentwechat.wechat_test

    wechat_test.short_description = "开通心理测评"

    def wechat_date2(self):
        return self.student.studentwechat.wechat_date2

    wechat_date2.short_description = "开通日期"

    def onduty(self):
        return self.student.onduty.onduty
    onduty.short_description="出勤率"

    def homework(self):
        return self.student.onduty.homework

    homework.short_description = "视频提交"

    def other(self):
        return self.student.onduty.other

    other.short_description = "备注"

    def exam_date(self):
        return self.student.studentexam.exam_date

    exam_date.short_description = "参试时间"

    # def exam_theory(self):
    #     return self.student.studentexam.exam_theory
    #
    # exam_theory.short_description = "理论报考"

    def exam_theory_result(self):
        return self.student.studentexam.exam_theory_result

    exam_theory_result.short_description = "国考理论总分"

    # def exam_practise(self):
    #     return self.student.studentexam.exam_practise
    #
    # exam_practise.short_description = "实操报考"

    def exam_practise_result(self):
        return self.student.studentexam.exam_practise_result

    exam_practise_result.short_description = "国考实操总分"


    def exam_practise_result2(self):
        return self.student.studentexam.exam_practise_result2

    exam_practise_result2.short_description = "实操笔试分"

    def exam_pre(self):
        return self.student.studentexam.exam_pre

    exam_pre.short_description = "说课分"

    def exam_speech(self):
        return self.student.studentexam.exam_speech

    exam_speech.short_description = "宣讲分"

    def exam_thr_theory(self):
        return self.student.studentexam.exam_thr_theory

    exam_thr_theory.short_description = "协会三级理论"

    def exam_thr_skill(self):
        return self.student.studentexam.exam_thr_skill

    exam_thr_skill.short_description = "协会三级技能"

    def exam_sec_theory(self):
        return self.student.studentexam.exam_sec_theory

    exam_sec_theory.short_description = "协会二级理论"

    def exam_sec_skill(self):
        return self.student.studentexam.exam_sec_skill

    exam_sec_skill.short_description = "协会二级技能"

    def exam_thesis(self):
        return self.student.studentexam.exam_thesis

    exam_thesis.short_description = "协会论文答辩"

    def exam_CAS(self):
        return self.student.studentexam.exam_CAS

    exam_CAS.short_description = "中科院成绩"

    def exam_other(self):
        return self.student.studentexam.exam_other

    exam_other.short_description = "备注"

    # def exam_total(self):
    #     return self.student.studentexam.exam_total
    #
    # exam_total.short_description = "综合报考"

    # def exam_total_result(self):
    #     return self.student.studentexam.exam_total_result
    #
    # exam_total_result.short_description = "综合成绩"
    #
    # def exam_status(self):
    #     return self.student.studentexam.exam_status
    #
    # exam_status.short_description = "合格情况"
    #
    # def exam_date_extra(self):
    #     return self.student.studentexamextra.exam_date
    #
    # exam_date_extra.short_description = "补考理论日期"
    #
    # def exam_theory_extra(self):
    #     return self.student.studentexamextra.exam_theory
    #
    # exam_theory_extra.short_description = "补考理论报考"
    #
    # def exam_theory_result_extra(self):
    #     return self.student.studentexamextra.exam_theory_result
    #
    # exam_theory_result_extra.short_description = "补考理论成绩"
    #
    # def exam_practise_extra(self):
    #     return self.student.studentexamextra.exam_practise
    #
    # exam_practise_extra.short_description = "补考实操报考"
    #
    # def exam_practise_result_extra(self):
    #     return self.student.studentexamextra.exam_practise_result
    #
    # exam_practise_result_extra.short_description = "补考实操成绩"
    #
    # def exam_total_extra(self):
    #     return self.student.studentexamextra.exam_total
    #
    # exam_total_extra.short_description = "补考综合报考"
    #
    # def exam_total_result_extra(self):
    #     return self.student.studentexamextra.exam_total_result
    #
    # exam_total_result_extra.short_description = "补考综合成绩"
    #
    # def exam_status_extra(self):
    #     return self.student.studentexamextra.exam_status
    #
    # exam_status_extra.short_description = "补考合格情况"

    def cert_id(self):
        return self.student.studentcertification.cert_id

    cert_id.short_description = "协会证书编号"
    #
    # def cert_date(self):
    #     return self.student.studentcertification.cert_date
    #
    #
    # cert_date.short_description = "发证日期"

    def cert_draw_people(self):
        return self.student.studentcertification.cert_draw_people

    cert_draw_people.short_description = "领取人"

    def cert_draw_date(self):
        return self.student.studentcertification.cert_draw_date

    cert_draw_date.short_description = "领取时间"

    def cert_nation_id(self):
        return self.student.studentcertification.cert_nation_id

    cert_nation_id.short_description = "国证编号"

    def cert_nation_people(self):
        return self.student.studentcertification.cert_nation_people

    cert_nation_people.short_description = "国证领取人与日期"

    def cert_CAS_id(self):
        return self.student.studentcertification.cert_CAS_id

    cert_CAS_id.short_description = "中科院证书编号"

    def cert_CAS_people(self):
        return self.student.studentcertification.cert_CAS_people

    cert_CAS_people.short_description = "中科院证书领取人与日期"

    def cert_other(self):
        return self.student.studentcertification.cert_other

    cert_other.short_description = "备注"





