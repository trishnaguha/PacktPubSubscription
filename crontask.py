import logging
from crontab import CronTab

"""
Job Scheduler
"""

class CronManager(object):

    def __init__(self):
        self.cron = CronTab(user=True)

    def daily_job(self, name, user, command, environment=None):
        """
        Add a daily cron task
        """
        cron_job = self.cron.new(command=command, user=user)
        cron_jon.minute.on(30)
        cron_job.hour.on(20)
        cron_job.enable()
        self.cron.write()
        if self.cron.render():
            print(self.cron.render())
            return True



