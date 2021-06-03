from django.contrib.auth.models import User

class EmailAuth:
    """ authenticate a user by an exact match on email and password"""
    
    def authenticate(self, username=None, password=None):
        """Get an istance of 'user' based off the email and verify password"""
        
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """used be the django auth system to retrieve a user instance"""
        
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
            
        except User.DoesNotExist:
            return None
                
        
    