A cloud-hosted web-app for a car dealership's car reviewal platform
This repo contains the code for a Django web application hosted in the IBM Cloud.

Background
I developed the application as part of the final Capstone Project in the 12-course IBM Full Stack Cloud Developer Professional Certificate on Coursera. I was provided an initial rudimentary version of the Django application, without any central functionality or templates. The general architecture and idea for the application was provided by Coursera, as well as most of the design and layout. Since the project was peer-reviewed after strict requirements.

Project Requirements
The Project is to build a website that allows users to select one of Best Car's dealerhips (a fictional company) in the US to view other users' reviews of the dealership's cars, as well as submit their own reviews. The site also needed basic functionality such as a navigation bar and static "about" and "contact" pages. The website had to be built with the Python-Django full stack web development framework and be deployed with Red Hat Openshift/Kubernetes on the IBM Cloud.

Architecture
Application architecture model Application architecture


![capstone-project-model](https://github.com/Babes2345/xrwvm-fullstack_developer_capstone/assets/86923935/9354d399-b879-4cae-bee1-898cff3085e7)

The dealership and review data is located in an IBM Cloudant database, while data about users and cars is in a simple SQLite database. In order to access data from IBM Cloudant, I wrote three IBM Cloud Functions which were accessible through an API.

Each review is analysed by IBM Watson in order to display the review's general sentiment (negative, neutral, positive).

Setup
Clone the project:

cd Full\ Stack\ Cloud\ Dev\ Capstone\ Project/server Install the required Python packages
python -m pip install -r requirements.txt
Create a new Django Secret Key

Run the development server:

python manage.py createmigrations
python manage.py migrate
python manage.py runserver
Create a new superuser:

python manage.py createsuperuser
Log in via the admin site (just add /admin at the end of the url)
Push to IBM Cloud Foundry:

Install the IBM Cloud CLI and the cloud foundry plugin
Configure the manifest.yml file
ìbmcloud cf push

