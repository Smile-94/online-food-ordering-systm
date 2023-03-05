def category_directory_path(instance,filename):
    return 'Catagory{0}/{1}'.format(instance.user.email,filename)