import os
import logging
from crontab import CronTab

"""
Job Scheduler
"""

'''class CronManager(object):

    def __init__(self):
        self.cron = CronTab(user=True)

    def daily_job(self, name, user, command, environment=None):
        """
        Add a daily cron task
        """
        cron_job = self.cron.new(command=command, user=user)
        cron_job.minute.on(52)
        cron_job.hour.on(12)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print(self.cron.render())
            return True

job = CronManager()
job.daily_job('root', 'python manage.py runserver')'''

CURR_DIR = os.getcwd()

cron = CronTab(user='trishna')

cmd = 'source {0}/venv/bin/activate && python {0}/manage.py runserver'.format(CURR_DIR)

job  = cron.new(command=cmd)
job.minute.on(30)
job.hour.on(20)

#writes content to crontab
cron.write('cronlog.tab')
print cron.render()
