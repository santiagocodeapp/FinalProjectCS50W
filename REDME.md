# CS50’s Web Programming with Python and JavaScript Final Project

Hello, my name is Santiago Nessy.

Before talking about the project I want to give you a bit of context. I played Professional Baseball for 12 years and in 2018 I became a Coach at [IMG Academy](https://www.imgacademy.com). Here at IMG we have a very high flow of athletes that come and go throughout the year and we always have to give them a report on how their performance was during their stay at IMG, this is usually done by sending an email to the parents and That's all problem solved but as a former Player I ask you how many times do we not understand or simply forget what our Coach tells us or explains? How many days go by without having a clear vision of how or when to make an adjustment that will help us improve? So as a Coach I asked myself how we can improve communication between students/athletes and Coaches and make our work as coaches a little easier? And as a player, how can I easily understand what my Coach wants to tell me or how do I remember everything that my Coach wants me to remember? and it was there when it occurred to me to make a web application called IMGReportApp where at the end of the day I can enter and write a brief report about my athletes where I can let them know how they did it or what are the things that they need to improve among many other things .

With this product it becomes easier for us coaches to maintain constant communication with the athletes and we can easily keep a record of the athletes' development and the athletes will find it easier to understand and put into practice all those things that we simply sometimes forget and undermines the development of athletes.



## IMGReportApp 

IMGReportApp is split into 2 main paths "/coach" and "/student".

***"/coach"***  is the route that serves coaches and will allow them to use the functions of creating teams, players and sending daily reports to athletes. Coaches can register and login and start writing reports to players.

***"/students"*** is the path that serves students/athletes. This route is simple since the students will only be able to read the report written by the coaches. In the future I would like the athletes to be able to evaluate the reports and ask for clarification if they do not understand 100% what the coach wrote.



# Understanding The Files

## FinalProject
This is the main Django Project where two applications are generated, the first called MyReport and the second Student

## MyReport:
### views.py:
#### index:
Returns the list of all teams created and saved in the database as long as the user is logged in.
#### login_view:
Authenticate the login of the users with the database in order to gain access.
#### logout_view:
Log out users
#### register:
Register new users. It asks for their username, first name, last name, email, and password. All these fields are required to send the form. If they do not pass the validation, the new users will not be able to be registered.
#### send_report:
This function is responsible for saving the report in the database. The fields are required on the frontend. At the end, the Team function returns, which is responsible for rendering the teams.
#### team:
This function takes as an argument the name of the team that will then be used to call the database and return all the players that belong to that team.
#### add_player:
This function is responsible for creating new players in the database and assigning them to teams already created in the database.
#### add_team:
This function is responsible for creating new teams that will later be filled with players. This way we can organize the players and the different coaches can go directly to their teams and get their players there.


### templates/MyReport:
#### ***layout.html:***
This is the main HTML file from which the other files will extend. Here is the JavaScript code and everything and 2 Modal that will be used a lot while using the page.
#### ***index.html:***
Several blocks extend into this file. We have the template container that will serve to render the different teams. We also have 2 blocks that extend from the layout.html that will serve to keep the modals updated.
Here I also add two separate scripts that will let the user know when they create a new team or when they add a new one.
#### ***team.html:***
Here is the template that will be generated dynamically according to how many players are on that team. If there are no players on that team an alert will be rendered letting the coach know that there are no players and that they need to be added, then they will be returned to the page where you see the teams.
#### ***login.html/register.html:***
This also extends from layout.html and there are only two forms to fill out in order to register or login.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.