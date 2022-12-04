from django.urls import path
from . import views


urlpatterns = [                   
                        path('about',views.about, name='about'),
                    path('assets',views.assets, name='assets'),
                    path('contact',views.contact, name='contact'),
                    path('faq',views.faq, name='faq'),
                    path('',views.index, name='index'),
                        path('payment_policy',views.payment_policy, name='payment_policy'),
                    path('privacy_policy',views.privacy_policy, name='privacy_policy'),
                    path('terms_and_conditions',views.terms_and_conditions, name='terms_and_conditions'),
                    
    ]
    #urls created                   
                        