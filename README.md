# PhotoAPI

RESTful API that downloads photos from FlickrAPI and then exposes them at respective endpoints.

### Installation instructions - 

1. Clone the repository

2. Install 'virtualenv' to create a virtual environment for our API

   `pip install virtualenv`

3. Setup the virtual environment

   `virtualenv sample_name_for_virtual_env`

4. Activate the virtual environment

   `sample_name_for_virtual_env\Scripts\activate`

5. Install the dependencies

   `pip install -r requirements.txt`

6. Set up the database (first change to the UrlCrawler directory)

   `python manage.py makemigrations`


   `python manage.py migrate`

7. Run the server (on localhost:8000)

   `python manage.py runserver`
   
### Setting up the database -

1. Launch the Django shell
	
	`python manage.py shell`

2. Import the populateDbExample file. (Make sure to add your API key in this file in the appropriate place)

	`import populateDbExample`

3. The database is populated with the provided groups and photos from FlickrAPI.		

### API reference - 

**End point** - api/v1/groups/

**Methods allowed** - GET

Returns all the groups available in the database.

**End point** - api/v1/group/&ltgid&gt/

**Methods allowed** - GET

Returns all the photo ids that are part of the provided group id.

**End point** - api/v1/photo/&ltpid&gt/

**Methods allowed** - GET

Returns the data related to a particular photo id.

**End point** - api/v1/login/ and api/v1/logout/ 

**Methods allowed** - POST

Authentication end points for the REST API.