from .models import Graditude, User 

def getUserGrats():
    name = 'Adi'
    user = User.objects.get(pk=1)

    #normally, we would query for the active user and a date range
    all_entries = Graditude.objects.all()

    txt = ''
    for entry in all_entries:
        txt = txt + entry
    
