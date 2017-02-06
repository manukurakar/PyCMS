from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from editor.models import article


# Create your views here.

class EditorView(View):
    def get(self,request):
        return render(request,'editor.html')

    def post(self,request):
        rcvd_rqst = request.POST
        eng_english = self.save_data(rcvd_rqst)
        return HttpResponse("Data Saved")

    def save_data(self,my_request):
        english_title = my_request.get('head_english')
        local_title = my_request.get('head_lc_lang')
        content = my_request.get('content')

        # Save data to database
        save_content = article(article_heading=english_title,
                                     article_head_lc_lang=local_title,
                                     article=content)
        save_content.save()

class HomeView(View):
    def get(self,request):
        data = article.objects.all()
        context = {
            'context_data' : data
        }
        return render(request,'front_page.html',context)