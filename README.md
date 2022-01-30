# CustomUserModel
custom user model with AbstractBaseUser and baseusermanager
created the user models from the AbstractBaseUser
define the manager for the usermodel

use PermissionMixin

from the admin.py override the all template in django admin 
added the testing using the coverage package 
coverage  run --omit='/*env*/'  manage.py test
coverage html 
