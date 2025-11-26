from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row


# class SkillWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','','','','','',''])

# class SkillsField(forms.MultiValueField):
# 	widget=SkillWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


# class ExpWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class ExpField(forms.MultiValueField):
# 	widget=ExpWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'

# class EduWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class EduField(forms.MultiValueField):
# 	widget=EduWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'


class ContactForm(forms.Form):
	name=forms.CharField()
	job_title=forms.CharField(required=False)
	email=forms.EmailField(label='E-Mail')
	mobile=forms.CharField()
	address=forms.CharField()
	linkedin=forms.CharField(required=False,label='LinkedIn URL')
	portfolio=forms.CharField(required=False,label='Portfolio / Website')
	github=forms.CharField(required=False,label='GitHub URL')
	summary=forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required=False,label='Professional Summary')

	skills_1=forms.CharField()
	skills_2=forms.CharField()
	skills_3=forms.CharField(required=False)
	skills_4=forms.CharField(required=False)

	experience_1_title=forms.CharField(label='Experience Title')
	experience_1_dur=forms.CharField(label='Duration')
	experience_1_desc=forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label='Description')

	experience_2_title=forms.CharField(required=False,label='Experience Title')
	experience_2_dur=forms.CharField(required=False,label='Duration')
	experience_2_desc=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':3}),label='Description')

	project_1_title=forms.CharField(label='Highlighted Project')
	project_1_desc=forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label='What did you build?')
	project_1_link=forms.CharField(required=False,label='Project Link')
	project_2_title=forms.CharField(required=False,label='Secondary Project')
	project_2_desc=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':3}),label='What did you build?')
	project_2_link=forms.CharField(required=False,label='Project Link')

	education_1=forms.CharField()
	education_1_dur=forms.CharField()
	education1_score=forms.CharField(label='Score / GPA')

	education_2=forms.CharField()
	education_2_dur=forms.CharField()
	education2_score=forms.CharField(label='Score / GPA')

	certifications=forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':2}),label='Certifications (comma separated)')
	hobbies=forms.CharField(required=False,label='Hobbies / Interests')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_class = ' container justify-content-center '
		# self.helper.label_class = ''
		# self.helper.field_class = 'col-md-6 col-xs-9'
		self.helper.form_method="post"
		self.helper.layout=Layout(
			Row(
                Column('name', css_class='form-group col-md-4 mb-10'),
                Column('job_title', css_class='form-group col-md-4 mb-10'),
                Column('email', css_class='form-group col-md-4 mb-10'),
                css_class='form-row center'
            ),
			Row(
                Column('mobile', css_class='form-group col-md-4 mb-10'),
                Column('address', css_class='form-group col-md-4 mb-10'),
                Column('linkedin', css_class='form-group col-md-4 mb-10'),
                css_class='form-row center'
            ),
			Row(
                Column('portfolio', css_class='form-group col-md-6 mb-10'),
                Column('github', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			'summary',
			Row(
                Column('skills_1', css_class='form-group col-md-6 mb-10'),
                Column('skills_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			Row(
                Column('skills_3', css_class='form-group col-md-6 mb-10'),
                Column('skills_4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			Row(
                Column('experience_1_title', css_class='form-group col-md-7 mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row center'
            ),
			'experience_1_desc',
			Row(
                Column('experience_2_title', css_class='form-group col-md-7 mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row center'
            ),
			'experience_2_desc',
			Row(
                Column('project_1_title', css_class='form-group col-md-6 mb-10'),
                Column('project_1_link', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			'project_1_desc',
			Row(
                Column('project_2_title', css_class='form-group col-md-6 mb-10'),
                Column('project_2_link', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			'project_2_desc',
			'education_1',
			Row(
                Column('education_1_dur', css_class='form-group col-md-6 mb-10'),
                Column('education1_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			'education_2',
			Row(
                Column('education_2_dur', css_class='form-group col-md-6 mb-10'),
                Column('education2_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			Row(
                Column('certifications', css_class='form-group col-md-6 mb-10'),
                Column('hobbies', css_class='form-group col-md-6 mb-10'),
                css_class='form-row center'
            ),
			Submit('submit','Submit',css_class="btn-success")
		)