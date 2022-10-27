<H1>Task application developed with Flask</H1>
<p>In this porject were used: Flask, sqlite3, html, css</p>
<H3>Project Structure</H3>
-------------------------------------------------------------------------------
├───static              <- folder with the static files CSS, Images, JavaScript 
│   ├───css
│   │    └───main.css
│   ├───img
│   └───js
│          
├───templates           <- HTML files. login and task extends from main
│        └───login.html
│        └───main.html
│        └───task.html
│ 
├───_config.py       <-File with the configuration to the flask application, Users,Database
├───db_create.py        <-Run to create the database and table
├───forms.py            <- Form use in task template
├───requirements.txt
├───run.py              <- Execute this file to run the application
├───task.db             <- Database to save the tasks
└───views.py            <- The logic of the web
-------------------------------------------------------------------------------
