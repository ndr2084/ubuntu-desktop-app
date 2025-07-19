import os
import subprocess
from Repo.app_repo import AppRepo

APPLICATION_DICT = {
    'pycharm' : './Apps/pycharm-2025.1.3.1/bin/pycharm'
    }
class AppService:
    def __init__(self, app_repo: AppRepo):
        self.repo = app_repo
        self.DEFAULT_DIRECTORY = os.path.expanduser("~")
        os.chdir(self.DEFAULT_DIRECTORY)

    @staticmethod
    def open_application(key):
        print(os.path.exists(APPLICATION_DICT.get(key)))
        if key in APPLICATION_DICT and os.path.exists(APPLICATION_DICT.get(key)):
            return AppService.run_command(key)
        else:
            return AppService.run_command(APPLICATION_DICT['DEFAULT'])

    @staticmethod
    def run_command(cmd):
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Exit Code:", result.returncode)
        return result.returncode

    @staticmethod
    def terminate_port():
        return None

    @staticmethod
    def add_to_path():
        return None

    @staticmethod
    def reboot_to_uefi():
        return None