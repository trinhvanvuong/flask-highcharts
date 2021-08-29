heroku create flask-highcharts --buildpack heroku/python
git push heroku master
heroku ps:scale bot=1 