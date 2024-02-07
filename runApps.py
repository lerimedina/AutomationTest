#Script for launching multiple applications

import AppOpener as ao

def run_apps(apps):
    for app in apps:
        ao.open(app, match_closest=True)

run_apps(["chrome"])