import requests
import sys
def getFile(url):
    try:
        data = requests.get(url)
        if not (data.status_code == 200 or data.status_code == 301):
            print("URL: " + str(data.status_code))
            sys.exit()
        return data.text
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit()


from jinja2 import Template, Environment, FileSystemLoader
import shutil
import yaml
import os
def parseAlerts(yamlFile):
    alerts = []

    ymlData = yaml.load(yamlFile)
    for alerts_array in ymlData['spec']['groups']:
        alerts.append(alerts_array['rules'][0])

    return alerts


def generateMarkdown(alertList, templateFile):
    outputDirectory = "Alerts"
    if os.path.exists(outputDirectory):
        shutil.rmtree(outputDirectory)
    os.mkdir(outputDirectory)

    for alerts in alertList:
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(templateFile)
        rendered = template.render(alert=alerts)

        with open(outputDirectory + "/" + alerts['annotations']['wiki_path'] + ".md", 'w') as data:
            data.write(str(rendered))


if len(sys.argv) == 2:
    yamlUrl = sys.argv[1]
    generateMarkdown(parseAlerts(getFile(yamlUrl)), "_TEMPLATE.md")
    # getFile(yamlUrl)
else:
    print("Specify the URL of prometheus-rules.yaml as an argument.")
