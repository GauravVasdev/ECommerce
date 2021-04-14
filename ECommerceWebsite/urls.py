from django.urls import path
from . import views

urlpatterns =[
    path('',views.homepage,name="homepage"),
    path('men_items/',views.men_items,name="men_items"),
    path('women_items/',views.women_items,name="women_items"),
    path('Loginforecommerce/',views.loginforecommerce,name="loginforecommerce"),
    path('Registerforecommerce/',views.Registerforecommerce,name="Registerforecommerce"),
    path('menTshirtCollection/menT-shirtcollection/',views.mentshirtcollection,name="menTshirtCollection/menT-shirtcollection"),
    path('menShoesCollection/menshoescollection/',views.menshoescollection,name="menShoesCollection/menshoescollection"),
    path('menWatchCollection/menwatchescollection/',views.menwatchcollection,name="menWatchCollection/menwatchescollection"),
    path('menSunglassesCollection/mensunglassescollection/',views.mensunglassescollection,name="menSunglassesCollection/mensunglassescollection"),
    path('menjeansCollection/menjeanscollection/',views.menjeanscollection,name="menjeansCollection/menjeanscollection"),
    path('menPerfumeCollection/menperfumecollection/',views.menperfumecollection,name="menPerfumeCollection/menperfumecollection"),
    path('womentshirtcollection/womentshirtcollection/',views.womentshirtcollection,name="womentshirtcollection/womentshirtcollection"),
    path('womenshoescollection/womenshoescollection/',views.womenshoescollection,name="womenshoescollection/womenshoescollection"),
    path('womenwatchescollection/womenwatchescollection/',views.womenwatchcollection,name="womenwatchescollection/womenwatchescollection"),
    path('womensunglassescollection/womensunglassescollection/',views.womensunglassescollection,name="womensunglassescollection/womensunglassescollection"),
    path('womenjeanscollection/womenjeanscollection/',views.womenjeanscollection,name="womenjeanscollection/womenjeanscollection"),
    path('womenperfumecollection/womenperfumecollection/',views.womenperfumecollection,name="womenperfumecollection/womenperfumecollection"),
    path('Cartforecommerce/',views.Cartforecommerce,name="Cartforecommerce"),
    path('checkoutpageforecommerce/',views.checkoutpageforecommerce,name="checkoutpageforecommerce"),
    path('addtocartajaxrequest/',views.addtocartajaxrequest,name="addtocartajaxrequest"),
    path('downitembyajaxrequest/',views.downitembyajaxrequest,name="downitembyajaxrequest"),
    path('checkoutshippinginformation',views.checkoutshippinginformation,name="checkoutshippinginformation")
]