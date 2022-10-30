from django.urls import path
from users import views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup_view"),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), #로그인 할 때 씀
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:id>/follow/',views.FollowView.as_view(), name="follow_view"),
    path('<int:id>/profile/', views.ProfileView.as_view(), name="profile_view"),
]