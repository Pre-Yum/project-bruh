  
from django.urls import path

from friend.views import(
	send_friend_request,
    friend_requests,
    accept_friend_request,
    decline_friend_request,
    remove_friend,
    cancel_friend_request,
    friends_list_view,
)

app_name = 'friend'

urlpatterns = [
    path('list/<user_id>/', friends_list_view, name='list'),
    path('friend_remove/', remove_friend, name='remove-friend'),
    path('friend_requests/', send_friend_request, name='friend-request'),
    path('friend_requests_cancel/', cancel_friend_request, name='friend-request-cancel'),
    path('friend_requests/<user_id>/', friend_requests, name='friend-requests'),
    path('accept_friend_request/<friend_request_id>', accept_friend_request, name='friend-request-accept'),
    path('decline_friend_request/<friend_request_id>', decline_friend_request, name='friend-request-decline'),
    
]