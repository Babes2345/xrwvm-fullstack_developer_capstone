# Full Stack Django Cloud Project
### _A cloud-hosted web-app for a car dealership's car reviewal platform_
This repo contains the code for a Django [web application](https://sr-django-capstone.eu-de.mybluemix.net/djangoapp/) hosted in the IBM Cloud.

#### Background:
I developed the application for my final [Capstone Project](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone?specialization=ibm-full-stack-cloud-developer)  as part of the [IBM Full Stack Cloud Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer), a 12-course program offered on Coursera. Initially, I was given a basic version of a Django application that lacked central functionality and templates. The overarching architecture and concept for the application were outlined by Coursera, along with the majority of the design and layout. The project underwent rigorous peer review, adhering to strict requirements set by the course.

#### Project Requirements:
The project involved creating a website for Best Car's dealerships, a fictional entity, enabling users across the US to browse and post reviews about the dealership's vehicles. Essential features required for the site included a navigation bar and static pages for "about" and "contact" information. The website was to be developed using the Python-Django full stack web development framework and deployed using Red Hat Openshift/Kubernetes on the IBM Cloud.

#### Architecture:
![capstone-project-model](https://github.com/Babes2345/xrwvm-fullstack_developer_capstone/assets/86923935/9354d399-b879-4cae-bee1-898cff3085e7)
_Application architecture model Application architecture_


The dealership and review data is located in an IBM Cloudant database, while data about users and cars is in a simple SQLite database. In order to access data from IBM Cloudant, I wrote three IBM Cloud Functions which were accessible through an API.

Each review is analysed by IBM Watson in order to display the review's general sentiment (negative, neutral, positive).

#### Setup 
Clone the project:
- ```cd Full\ Stack\ Cloud\ Dev\ Capstone\ Project/server```
Install the required Python packages
- ```python -m pip install -r requirements.txt```

Create a [new Django Secret Key](https://humberto.io/blog/tldr-generate-django-secret-key/) 

Run the development server: </br>
- ```python manage.py createmigrations```
- ```python manage.py migrate```
- ```python manage.py runserver```

Create a new superuser:
- ```python manage.py createsuperuser```
- Log in via the admin site (just add `/admin` at the end of the url)

Push to IBM Cloud Foundry:
- Install the IBM Cloud CLI and the cloud foundry plugin
- Configure the `manifest.yml` file
- `ìbmcloud cf push`

Install the IBM Cloud CLI and the cloud foundry plugin
Configure the manifest.yml file
ìbmcloud cf push

