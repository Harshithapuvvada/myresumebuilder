from django.shortcuts import render
from .forms import ContactForm

def home(request):
	return render(request, 'home.html', {})

def info(request):
	form=ContactForm()
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cleaned = {field: form.cleaned_data.get(field, '') for field in form.fields}
			certifications = [
				item.strip() for item in cleaned.get('certifications', '').split(',')
				if item.strip()
			]
			hobbies = [
				item.strip() for item in cleaned.get('hobbies', '').split(',')
				if item.strip()
			]
			projects = [
				{
					'title': cleaned.get('project_1_title'),
					'description': cleaned.get('project_1_desc'),
					'link': cleaned.get('project_1_link'),
				},
				{
					'title': cleaned.get('project_2_title'),
					'description': cleaned.get('project_2_desc'),
					'link': cleaned.get('project_2_link'),
				}
			]
			context = {**cleaned}
			context['certification_list'] = certifications
			context['hobby_list'] = hobbies
			context['projects'] = [p for p in projects if p['title'] or p['description']]
			return render(request,'home.html',context)
	return render(request,'info.html',{'form':form})
