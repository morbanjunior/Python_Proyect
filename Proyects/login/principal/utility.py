from .models import User

#this def is if you want to change the user's password
def update_pwd(username, pvd):
    user_model = User.objects.get(username = username)
    user_model.set_password(pvd)
    user_model.save()

class Messages:
    def __init__(self):
        self.message = ''
    
    message = ''
    tag = ''

#use for the message on html
def custom_message(message,tag):
    # 1.-success, 2.-info, 3.-warning 4.-danger
    msg = Messages()
    if tag ==0:
        msg.tag = "alert alert-success"
    
    elif tag == 1:
        msg.tag == "alert alert-info"
    
    elif tag == 2:
        msg.tag = "alert alert-warning"
    
    else:
        msg.tag = "alert alert-danger"

    return msg

class TagType:
    def __init__(self):
        pass

    success, info, warning, danger = range(4)