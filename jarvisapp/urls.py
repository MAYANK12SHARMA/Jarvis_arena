from django.urls import path
from jarvisapp import views



urlpatterns = [

#? ------------------------------- index ------------------------------- ?#
    path("", views.index, name="index"),
    
#! ------------------------------- index  End ------------------------------- ?#
    
#? ------------------------------- Developers ------------------------------- ?# 
   
    path("developer/mayank", views.mayank, name="mayank"),
    path("developer/jatin", views.jatin, name="jatin"),
    path("developer/arjun", views.arjun, name="arjun"),
    path("developer/vaishvik", views.vaishvik, name="vaishvik"),
    path("developer/garvit", views.garvit, name="garvit"),
    path("developer/parth", views.parth, name="parth"),

#! ------------------------------- Developers End ------------------------------- ?# 

#? ------------------------------- Services ------------------------------- ?#
  
    path("services/join_us", views.join_us, name="join_us"),
    path("services/contact_us", views.contact_us, name="contact_us"),

#! ------------------------------- Services End ------------------------------- ?# 

#? ------------------------------- Registration ------------------------------- ?#
  
    path('authrization/login/', views.login_attempt, name='login_attempt'),
    path('authrization/register/', views.register_attempt, name='register_attempt'),
    path('authrization/verify/<auth_token>', views.verify, name='verify'),
    path('authrization/logout/', views.logout_attempt, name='logout'),
    path('authrization/error/', views.error_page, name='error_page'),
    path('authrization/forget_password/', views.forget_password, name='forget_password'),
    path('authrization/change_password/<auth_token>/', views.change_password, name='change_password'),

#! ------------------------------- Registration End ------------------------------- ?#



#? ------------------------------- Games Dashboard ------------------------------- ?# 

    path('Games/allgames/', views.allgames, name='allgames'),
    path('Games/Brick_breaker/', views.Brick_breaker, name='Brick_breaker'),
    path('Games/Car_racing/', views.Car_racing, name='Car_racing'),
    path('Games/Flappy_Bird/', views.Flappy_Bird, name='Flappy_Bird'),
    path('Games/Go_ace/', views.Go_ace, name='Go_ace'),
    path('Games/Maze_solver/', views.Maze_solver, name='Maze_solver'),
    path('Games/Snake_game/', views.Snake_game, name='Snake_game'),
    path('Games/Space_invaders/', views.Space_invaders, name='Space_invaders'),
    path('Games/Sprite_flight/', views.Sprite_flight, name='Sprite_flight'),
    path('Games/Tic_Tac_toe/', views.Tic_Tac_toe, name='Tic_Tac_toe'),
    path('Games/Wach_a_mole/', views.Wach_a_mole, name='Wach_a_mole'),
   
    
    
    
    
    

]

