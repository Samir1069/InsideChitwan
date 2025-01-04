from allauth.socialaccount.models import SocialAccount

def get_profile_picture(user):
    social_account = SocialAccount.objects.filter(user=user, provider='google').first()
    if social_account:
        return social_account.extra_data.get('picture')
    return None
