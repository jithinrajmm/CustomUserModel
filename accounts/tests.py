from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class UserAccountTests(TestCase):

    # this testing for the superusercreations
    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'test@gmail.com','username','firstname','password'
        )

        self.assertEqual(super_user.email,'test@gmail.com')
        self.assertEqual(super_user.user_name,'username')
        self.assertEqual(super_user.first_name,'firstname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user),'username')

        # here we are going to check the value error that defined in the BaseUserManager
        with self.assertRaises(ValueError):
            db.objects.create_superuser(email = "testuser@gmail.com",user_name = 'username1',first_name = 'first_name',password='password',is_superuser=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(email = "testuser@gmail.com",user_name = 'username1',first_name = 'first_name',password='password',is_staff=False)

        # this method is used to testing the user
        def test_new_user(slef):
            db_user = get_user_model()
            user= db_user.objects.create_user('test@gmail.com','username','firstname','password')
            self.assertEqual(user.email, 'test@gmail.com')
            self.assertEqual(user.user_name,'username')
            self.assertEqual(user.first_name,'firstname')
            self.assertFalse(user.is_staff)
            self.assertFalse(user.is_active)
            self.assertFalse(user.is_superuser)


            with self.assertRaises(ValueError):
                db_user.objects.create_user(
                    email = '',user_name = 'username',
                    first_name = 'firstname',
                )







