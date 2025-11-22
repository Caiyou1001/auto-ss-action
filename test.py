from app.action import Action

email = 'contact@yanglibin.info'
passwd = 'xxxxxxxx'
host = 'cordc.co'
action = Action(email, passwd, host=host)
action.run()
