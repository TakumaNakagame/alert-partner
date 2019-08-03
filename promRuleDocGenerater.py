#!/usr/bin/python3

import sys
import modules

def main():
    if not len(sys.argv) == 2:
        print("Specify the URL of prometheus-rules.yaml as an argument.")
        sys.exit()

    prom_yaml = modules.get_template(sys.argv[1])
    if not prom_yaml.status:
        print("failed get")
        sys.exit()

    prom_rules = modules.parse_alerts(prom_yaml.response)
    if not prom_rules.status:
        print("failed parse")
        sys.exit()

    prom_generate = modules.generate_markdown(prom_rules.alerts, "_TEMPLATE.md")
    if not prom_generate.status:
        print("generate failed")

if __name__ == '__main__':
    main()