from django.urls import path
from api.views import get_classes, get_links, signup_user, login_user, GetUserData, SetRating, get_resources, \
  get_feedback, PostFeedback, verify_token, delete_rating, update_profile, recover_password, get_about, get_credits, \
  get_diagram

urlpatterns = [
  path('get/classes/', get_classes),
  path('get/links/', get_links),
  path('signup/', signup_user),
  path('login/', login_user),
  path('get/user-data/', GetUserData.as_view()),
  path('post/rating/', SetRating.as_view()),
  path('get/resources/', get_resources),
  path('get/feedback/', get_feedback),
  path('post/feedback/', PostFeedback.as_view()),
  path('verify-token/', verify_token),
  path('delete-rating/', delete_rating),
  path('update-profile/', update_profile),
  path('recover-password/', recover_password),
  path('get/about/', get_about),
  path('get/credits/', get_credits),

  path('get/diagram/', get_diagram),
]