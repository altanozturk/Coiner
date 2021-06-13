from django.urls import path
from . import views




urlpatterns = [
    path('', views.home),
    path('homepage/', views.home, name = "home"),
    path('aboutus/', views.aboutUs, name = "aboutus"),
    path('services/', views.services, name = "services"),
    path('happyhour/', views.happyhour, name = "happyhour"),
    path('buystocks/', views.buystocks, name = "buystocks"),
    path('signin/', views.signin, name = "signin"),
    path('signup/', views.signup, name = "signup"),
    path('user/<str:pk_test>/', views.user, name = "user"),
    path('stock/<str:pk>/', views.stock, name ="stock"),
    path('buying_stock/' , views.buyingStock , name ="buying_stock"),
    path('update_buy/<str:pk>/' , views.updateBuy , name ="update_buy"),
    path('delete_buy/<str:pk>/' , views.deleteBuy , name ="delete_buy"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('forum/<str:pk>/',views.forum,name="forum"),

    

    
    

    
    
    
]
