# Rajasthan-Hackathon-17 By Zero8

This idea is based on Bamashah yojna. In this application with the help of bhamashah data we will be integrating a scheme portal of government. As we know government issue a huge fund in braodcasting advert of Various Government policies. But still the people in remote ares are not able to get any Information regarding the Policy.
Our portal will use the data of Bhamashah to filter data and send Notification to Targeted End User.

Where End user can get all the information regarding policy and what are the eligibility for availing the Policy.
This is a Backend application which is fetching data from the Bhamashah API and saving them in the database. On this saved data we apply the process to filter the data on various criteria such Povery Line, Education.

The Front end of the Application is based on ReactJS. The backend is Python Based Django Framework. 

# Quick start:
# Install Virtual Environment
1) $ virtualenv venv
2) $ source /venv/bin/activate
# Install Dependencies
3) $ cd source
4) $ pip install -r requirements.txt
5) $ cd source
# Run the server
6) $ python manage.py runserver

For API please visit
Head of Family details
http://139.59.33.29:8000/api/info/?format=json

Family Member 
http://139.59.33.29:8000/api/familyinfo/?format=json

Scheme API
http://139.59.33.29:8000/api/scheme/?format=json
