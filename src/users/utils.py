def user_directory_path(instance, filename):
    return f"user_{instance.user.id}/{filename}"