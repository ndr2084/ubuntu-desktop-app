from Service.app_service import AppService

class AppController:
    def __init__(self, app_service: AppService):
        self.service = app_service

    def open_application(self, key):
        return self.service.open_application(key)

    def terminate_port(self):
        return self.service.terminate_port()

    def add_to_path(self):
        return self.service.add_to_path()

    def reboot_to_uefi(self):
        return self.service.reboot_to_uefi()

