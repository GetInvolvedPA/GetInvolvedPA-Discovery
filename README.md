# GetInvolvedPA-Discovery
A website for discovering community service organizations in Palo Alto. 

*add a screenshot here*

### Setup ###
Make sure you have git and python 2.7 installed on your computer. 

In your terminal, clone this repository:  
`git clone https://github.com/GetInvolvedPA/GetInvolvedPA-Discovery.git`

We are using [virtualenv](https://virtualenv.pypa.io/en/latest/) to manage our Python library versions as specified in `requirements.txt`. Make sure you have virtualenv installed by running `pip install virtualenv` or `sudo pip install virtualenv`, depending on how your system Python is installed. 

For the initial setup for virtualenv, run:  
`./setup.sh`

Every time you work on this project, you need to have the virtualenv loaded. This is indicated by `(.env)` in front of your shell prompt. If you do not see this, run: 
`source .env/bin/activate`

### Usage ###
First, enter the project subdirectory with `cd getInvolvedPAWebsite`  
Run the server with: `python manage.py runserver`  

