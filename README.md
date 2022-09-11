# Project 4: Python Django

*A full description of the project scope criteria can be found [here](https://sites.google.com/view/reference-page/project-4).*

---
**Name:  Ryan Stroemel**  
**Contact: rstroemel@gmail.com**  

---
 

YOUTRADE is a cryptocurrency trading application that allows individual users to perform hypothetical trading of Bitcoin for USD. YOUTRADE uses external API requests from [Alphavantage](https://www.alphavantage.co/documentation/) and [Cryptocompare](https://min-api.cryptocompare.com/documentation) APIs to pull real-time data for Bitcoin USD exchange rates, time series performance history data and news stories which may impact the price of Bitcoin. 

---

**Install instructions**

**1.**  Clone the repository
```
git clone https://github.com/ryandude97/project-4.git
```
**2.** Create a virtual environment in the cloned project directory
```
virtualenv django_project
```
**3.**  Activate the virtual environment
```
source project4/bin/activate 
```
**4.**  Install the dependencies from requirements.txt
```
pip install -r requirements.txt
```
**5.**  Collect the static files
```
python3 manage.py collectstatic
```
**6.**  Migrate the Database
```
python3 manage.py makemigrations app1
python3 manage.py migrate
```
**7.** Create a user account and log in
```
python3 manage.py createsuperuser
```
**8.** Run the dev server
```
python3 manage.py runserver
```
dev server address:  http://127.0.0.1:8000/

---

## Workflow Requirements

### User Stories:

**1.** 
I always buy the dip on crypto exchanges. Bitcoin for life. 
-Jason

**2.** 
I over-leverage my accounts all the time, so this $50,000 will be perfect to blow on crypto. 
-Julian

**3.** 
This app is better than CoinBase. The color schema and obvious bootstrap usage is amazing!
-Diavolo 

---

-- Development Phase:

**1.** Created Github repository [Project4](https://github.com/ryandude97/project-4)

**2.** Set up virtual environment locally, created a new Django project and app.

**3.** Developed static files and overall file structure, python.

**4.** Decided to use a pre-existing sqlite3 db crypto. 

**5.** Added miniaturized [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/download/) CSS and JS files, miniaturized [jQuery](https://jquery.com/download/), miniaturized [Plotly.js](https://plot.ly/javascript/getting-started/) charting library to the project static files folder.

**6.** pip installed python pandas, pandas-datareader, dash, django-plotly-dash and django-crispy-forms to the virtual envrionment.

**7.** Made python API requests to retrieve CSV and JSON data.

**8.** Created charts with python plotly and plotly.js to display data from the external APIs and from the Django database.

**9.** Created reg form with django-crispy-forms. 

**10.** Created account framework with $50,000.

**11.** Created a Transactions model that logs the transactions history of the authenticated user when trades are placed.  

**12.** Added a Reset button to allow the authenticated user to reset their Account balances and Transactions histories to their defaults.

**14.** Created an account interface that allows the authenticated user to track their portfolio performance by displaying account balances and chart data.

**15** Created realtime quotes and from rest api. 

