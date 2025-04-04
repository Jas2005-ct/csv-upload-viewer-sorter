# csv-upload-viewer-sorter
DJANGO APPLICATION UPLOAD CSV FILE AND DISPLAY THE DATA IN CSV AND SORTING
This is the Django web application that allows user to upload a csv file and sort based on the ascending or descending order depends upon the alphabetic and numeric order.

Features:
•	Simple upload of .csv file.
•	Clean UI using custom css.
•	Click on header to sort them in alphabetical or numerical.
•	Toggle sorting Algorthirm.

Technologies Used:
•	Django.
•	Python.
•	Pandas.
•	Html,css and js.

Optional Enhancement:
•	Add validation for file types (.csv only).
•	Display file name and row count.
•	Handle large CSVs with pagination.
•	Add filters/search input.
•	Export sorted data back to CSV.

Project Structure

hash/
│
├── excel/                    
│   ├── migrations/           
│   ├── static/               
│   ├── templates/hash/       
│   │   ├── home.html
│   │   ├── display.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── hash/               
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── media/                   
│   ├── uploads/
│
├── .gitignore                
├── db.sqlite3               
├── manage.py                 
├── requirements.txt          -- Dependencies list

