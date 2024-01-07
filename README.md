# data-representation-project

## Data Representation project 2023-2024
-----------

## Author: Sofiia Meteliuk G00426049
-----------

BIG PROJECT (60%)

Description:
Write a program that demonstrates that you understand creating and consuming
RESTful APIs. 

- Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
- You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.

### My project:
Simple shopping list, where you can write in product (`prod_name`) that you plan to buy, shop(`shop`) where to buy, and quantity (`quantity`).
It will be stored in database table (`sh_list`) in database called `shoppinglist`. 



### Repository contains: 

1. folder 'staticpages' with index.html for web application part and AJAX call to the server.
2. `server1.py` - a Flask server app program
3. `shoplistDAO.py` - DAO - Data Access Object - is a pattern that provides an abstract interface to the database
4. `dbconfig.py` and `.gitignore` 
5. `initdb.sql`- the sql code to create a database `shoppinglist` on your machine
6. `README.md` file
7. `requirments.txt` - file that contains all python packages with correct version to use with this project 

### To run this program on your machine:

1. Download zip file or clone this repository;
2. Open command line in project folder:
   - Print next commands to activate a virtual environment: `python -m venv venv`, then `.\venv\Scripts\activate.bat`; `pip install -r requirements.txt`;
3. Open mysql command line in project folder and repeat commands from `initdb.sql`;
3. Run `server1.py` from  command line. Go to page `http://127.0.0.1:5000/index.html`;
4. You can also see JSON file of current table  on `http://127.0.0.1:5000/items`;



-------
### References:
This project is based on code from: https://github.com/andrewbeattycourseware/datarepresentation/tree/main/code
