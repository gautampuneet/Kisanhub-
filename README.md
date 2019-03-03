Kisanhub Assignment

for using this first you have to install django,python,django rest frsmework in the system.

Then in the command line Run these commands.

1. python mangae.py runserver 
    
    It will start the project running then you can go to the localhost:8000/api-auth/api link on your browser to see the api.
    
2. python manage.py weatherreport

    It is the custom command which will fetch above json files for all the locations and metrics.
    
After this you can go to the browser and in the api  you should provide some parameters for the result. Which are

1. start_date
2. end_date
3.metric_type
4.location


For example:-   "http://localhost:8000/api-auth/api/?start_date=2000-01&end_date=2019-01&metric_type=Tmax&location=UK"

  This will output the data of UK-Tmax from jan 2000 to jan 2019
    
    
