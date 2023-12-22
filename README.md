# coding_test_mw

## Set up Django Project
Use requirments.txt to install essential modules for django framework. Setup a virtual environment. Also postgresql database is needed for database operations.

## Features and Functionalities
Task contains:
	a) Title, Description, Creation Date, Due Date, Priority and Mark (Multiple image integration is not implemented).
	
	b) Task can be searched by title in search box.
	
	c) Django authentication and login logout system is used. Also registration of new user is implemented. super user have to be created differently. Other user registrations are not super user.
	
	d) Filteration implemented in admin, not in showing the task.
	
	e) Different page for task deails based on user.
	
	f) Must be a user to add tasks.
	
## Database Relation
User is foreign key for task. One to many relation as one user can have many tasks but one task can not have many user.

## Admin
Models are added in admin. Functionality for accessing, updating and deleting data in added based on admin. Adding data is based on direct database implementation. Necessary fields are shown in admin. Tasks are sorted based on priority.

## Templates
One base template and other extends that same base template. Task list, creation, details, update and deletion all have different template. All are accessed by authorized user. Template tags are dynamic. Visually not appealing but adequate to an extent.

## Views
Classbased view implemented for rest framework. URL pattern done for views.

## Form
Task creating and update done with forms. Both custom and django forms are used. User validation and form validation implemented.

## REST API
Serializers used for json conversion, also appropriate HTTP methods used.

## Environment Variable
django environ used for environment variable. secret_key for django and user password of database is in .env file which is stored locally. To run, one must use their own enviroment in those cases. change env('option') to own to deal with environment variable.

## data.json
To use data, atleast 3 User needed.
