from django.apps import AppConfig
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command

class MeterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meter'

    def ready(self):
        # Start the scheduler in a separate thread
        scheduler_thread = threading.Thread(target=self.start_scheduler, daemon=True)
        scheduler_thread.start()

    def start_scheduler(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.update_readings_job, 'interval', minutes=1)
        scheduler.start()

        try:
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()

    def update_readings_job(self):
        # Call the custom management command to update meter readings
        call_command('update_meter_readings')