from django.urls import path
from . import views

app_name = 'green'

urlpatterns = [
    path('main/', views.main_view, name='main'),
    path('community/', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),
    path('test/', views.test, name='test'),
    path('list/', views.list, name='list'),
    path('expert/', views.expert, name='expert'),
    path('reserve/<int:expert_id>/', views.reserve, name='reserve'),
    path('reserve_ok/<int:expert_id>/', views.reserve_ok, name='reserve_ok'),
    path('reserve_complete/<int:expert_id>/', views.reserve_complete, name='reserve_complete'),
    path('market/', views.market, name='market'),
    path('external-link-ptech/', views.external_redirect_ptech, name='external_redirect_ptech'),
    path('external-link-heymoon/', views.external_redirect_heymoon, name='external_redirect_heymoon'),
    path('external-link-jiguhara/', views.external_redirect_jiguhara, name='external_redirect_jiguhara'),
    path('external-link-puliodays/', views.external_redirect_puliodays, name='external_redirect_puliodays'),
    path('external-link-costco/', views.external_redirect_costco, name='external_redirect_costco'),
    path('community/create/', views.community_create, name='community_create'),
    path('community/<int:post_id>/', views.community_detail, name='community_detail'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('community/<int:post_id>/comment/', views.comment, name='comment'),
    path('community/<int:post_id>/update/', views.community_update, name='community_update'),
    path('community/<int:post_id>/delete/', views.community_delete, name='community_delete'),
    path('premium-info/', views.premium_info, name='premium_info'),
    path('premium-ok/', views.premium_ok, name='premium_ok'),
    path('submit-payment/', views.submit_payment, name='submit_payment'),
    path('premium-complete/', views.premium_complete, name='premium_complete'),
    path('premium-payment-error/', views.premium_payment_error, name='premium_payment_error'),
    path('liked-posts/', views.liked_posts, name='liked_posts'),
    path('authored-posts/', views.authored_posts, name='authored_posts'),
    path('mypage/reservations/', views.reservation_list, name='reservation_list'),
]
