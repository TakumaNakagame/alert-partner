import requests
def getFile(url):
    try:
        data = requests.get(url)
        return data.text
    except requests.exceptions.RequestException as err:
        print(err)


from jinja2 import Template, Environment, FileSystemLoader
import os
import shutil


import yaml
def parseAlerts(yamlFile):
    alerts = []

    ymlData = yaml.load(yamlFile)
    for alerts_array in ymlData['spec']['groups']:
        alerts.append(alerts_array['rules'][0])

    return alerts


def addMD(alertList, templateFile):
    outputDirectory = "alerts"
    if os.path.exists(outputDirectory):
        shutil.rmtree(outputDirectory)
    os.mkdir(outputDirectory)

    for alerts in alertList:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(templateFile)
        rendered = template.render(alert=alerts)

        with open(outputDirectory + "/" + alerts['annotations']['wiki_path'] + ".md", 'w') as data:
            data.write(str(rendered))


import sys

if len(sys.argv) == 2:
    yamlUrl = sys.argv[1]
    addMD(parseAlerts(getFile(yamlUrl)), "_TEMPLATE.md")
else:
    print("Specify the URL of prometheus-rules.yaml as an argument.")
