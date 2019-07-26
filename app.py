import yaml

ymlSource = "data.yml"

result = []

with open(ymlSource, 'r') as yml:
    data = yaml.load(yml)

i = 0
for alerts_array in data['spec']['groups']:
    alert = alerts_array['rules'][0]
    print(i, end="")
    i += 1
    

    alert_title = alert['annotations']['title']
    print(alert_title)
    alert_severity = alert['labels']['severity']
    print(alert_severity)
    alert_about = alert['annotations']['wiki_about']
    print(alert_about)
    alert_threshold = alert['annotations']['wiki_threshold']
    print(alert_threshold)
    alert_impact = alert['annotations']['wiki_impact']
    print(alert_impact)
    alert_corresondence = alert['annotations']['wiki_corresondence']
    print(alert_corresondence)
    alert_expr = alert['expr']
    print(alert_expr)
    alert_for = alert['for']
    print(alert_for)

