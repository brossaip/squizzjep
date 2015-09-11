from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^enviador/', include('hello.urls')),
    url(r'^$', 'hello.views.home'),
)
