from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns =[
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9])/results/$', views.results, name='results' ),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 基于类的view，关联到views中一个继承django预定义的View类的类。
    # pk 作为参数传递到views的函数里，使用基于类的view，必须使用pk做为参数
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9])/results/$', views.ResultsView.as_view(), name='results' ),

    # 基于函数的view，关联到views中的函数
    # question_id 作为参数传递到views的vote函数里，使用基于函数的view可以自定义函数名
    # 当匹配到正则表达式后，通过以下方式调用view函数：vote(request=<HttpRequest object>, question_id='34')
    url(r'^(?P<question_id>[0-9])/vote/$', views.vote, name='vote'),
]
