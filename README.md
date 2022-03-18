# Django-AJAX-Logging-CRUD
CRUD Application using Django Framework
Important files:
- models.py file contains the model for user details (username, firstname, lastname, email).
- iews.py file contains the views required to represent the CRUD functionalities.
- db.sqlite3 id database file
- crud.html main page which has the following functionalities:
    - paginated list of all the users
    - buttons to request (GET/POST/PUT/DELETE/LOG)
    - click on buttons will show the respective form for request
    - on submitting the details respective response will be shown in the right side
    - on clicking LOG it will show the log.html page
- log.html
    - it has the paginated list of requests made on the crud.html page

Every functionality is developed using the AJAX only.



Functionalities
-	POST:
    -	Enter details as asked in the ADD user form and submit
    -	This will show the entered user details in the response section which is obtained from the json output
    -	Click on the number of the paginated list, all the user entries will be displayed
-	PUT:
    -	Enter the details that you want to UPDATE along with the userId. (Can be obtained by look in the paginated list view)
    -	Response will show the updated user details
    -	Again, click on the numbers in the paginated view to verify the updated details
-	GET:
    -	Enter the userId whose details you would like to view
    -	Response will show the user details of the corresponding userId
-	DELETE:
    -	Enter the userId whose details you would like to delete
    -	Response will show the user details of the deleted userId
    -	Click on the paginated numbers and verify that corresponding entry is deleted
-	LOGS:
    -	Click on log button, it will load the log.html page and will show a paginated list view of all the requests made in the main page (POST, PUT, GET, DELETE)
    -	Click on the page number to view the log details of the requests made by the user. It will show the Action (POST, PUT, etc), Id (user id that was affected/accessed         during this action), Time (time at which this action was performed)
