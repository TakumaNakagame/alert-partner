from jinja2 import Template, Environment, FileSystemLoader

def addMD(alertList, templateFile):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(templateFile)
    rendered = template.render(alert=alertList)
    print(str(rendered))


import yaml
def getAlerts(yamlFile):

    with open(yamlFile, 'r') as yml:
        data = yaml.load(yml)

    for alerts_array in data['spec']['groups']:
        alert = alerts_array['rules'][0]
        print(alert)
        return alert

addMD(getAlerts("data.yml"), "_TEMPLATE.md")