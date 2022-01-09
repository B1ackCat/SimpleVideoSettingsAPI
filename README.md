# SimpleVideoSettingsAPI
Simple VideoSettingsAPI H1

How to use:  
1.pip install -r requirements.txt  
2.Create Mysql DB "video_app" (Change Settings.py DataBase setting)  
3.python manage.py makemigrations  
4.python manage.py migrate  
5.python mange.py runserver  

URL LIST  
/VideoList/ : Show VideoList  
/VideoUpload/ : Upload Video  
/VideoList/{id} : Show Video<id> detail  
/VideoList/{id}/CommentList : Show CommentList 
/VideoList/{id}/CommentsList{no} : Show Comment{no} detail 
