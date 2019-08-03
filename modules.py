#!/usr/bin/python3

import os
import sys
import shutil
import requests
import yaml
from jinja2 import Template, Environment, FileSystemLoader

class get_template():

    def __init__(self, url):
        self.status: bool = False
        self.url: str = url
        self.response: str = ""
        self.get(url)

    def __check_url(self):
        pass

    def check_template(self):
        if not os.path.isfile("./_TEMPLATE.md"):
            print("Not found '_TEMPLATE.md' in current directory.")
            sys.exit()

    def get(self, url):
        self.__check_url()
        try:
            data = requests.get(url)
            if not (data.status_code == 200 or data.status_code == 301):
                print("URL: {}".format(data.status_code))
            else:
                self.response = data.text
                self.status = True
        except requests.exceptions.RequestException as err:
            print(err)

class parse_alerts():

    def __init__(self, alert_body):
        self.status: bool = False
        self.body: str = alert_body
        self.alerts: str = []
        self.parse(self.body)
        pass

    def __check_yaml(self) -> bool:
        result: bool = False
        pass
        result = True
        return result

    def parse(self, alert_body):
        if not self.__check_yaml():
            print("checking failed")
        yaml_body = yaml.load(alert_body)
        for alerts_array in yaml_body['spec']['groups']:
            self.alerts.append(alerts_array['rules'][0])

        self.status = True

class generate_markdown():
    def __init__(self, alerts, template_file):
        self.status: bool = False
        self.alert_body: str = alerts
        self.template_body: str = template_file
        self.directory_name: str = "Alerts"
        self.make_file_count: int = 0

        self.generate(self.alert_body, self.template_body)
        pass

    def __make_directory(self):
        if os.path.exists(self.directory_name):
            shutil.rmtree(self.directory_name)
        os.mkdir(self.directory_name)

    def generate(self, alerts, template_body):
        pass

        self.__make_directory()
        self.make_file_count = 0

        for alerts in alerts:
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template(template_body)
            rendered = template.render(alert=alerts)

            with open(self.directory_name + "/" + alerts['annotations']['wiki_path'] + ".md", 'w') as data:
                data.write(str(rendered))
            self.make_file_count += 1
        self.status = True
