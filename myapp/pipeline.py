def get_user_profile_picture(user, sociallogin, **kwargs):
    if sociallogin.account.provider == 'google':
        extra_data = sociallogin.account.extra_data
        user.profile_picture_url = extra_data.get('picture')  # Save or use this URL
        user.save()
