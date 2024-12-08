import argparse
import json
import os
import subprocess

def read_settings():
    with open("settings.json", "r") as settings:
        return json.load(settings)

def open_settings():
    subprocess.run("start settings.json", shell=True)

def pull_saves():
    curdir = os.getcwd()

    settings = read_settings()
    src = settings["saves_directory"]
    dest = os.path.abspath(settings["computer_directory"])

    if not os.path.exists(dest):
        os.mkdir(dest)
    return subprocess.run(f"{curdir}/platform-tools/adb.exe pull {src} {dest}", capture_output=True, text=True, shell=True)

def push_saves():
    curdir = os.getcwd()

    settings = read_settings()
    src = os.path.abspath(settings["computer_directory"])
    dest = settings["mobile_directory"]

    if not os.path.exists(src):
        os.mkdir(src)
    subprocess.run(f"{curdir}/platform-tools/adb.exe shell mkdir {dest}")
    return subprocess.run(f"{curdir}/platform-tools/adb.exe push {src} {dest}", capture_output=True, text=True, shell=True)

def main():
    parser = argparse.ArgumentParser(description="Stardew Valley Backup Tool")
    subparsers = parser.add_subparsers(dest="command", help="list of commands")
    subparsers.add_parser("pull", help="transfers saves from the device to the computer")
    subparsers.add_parser("push", help="transfers saves from the computer to the device")
    subparsers.add_parser("settings", help="opens settings.json")
    args = parser.parse_args()

    match args.command:
        case "pull":
            output = pull_saves()
            print(output.stdout if output.stdout else output.stderr)
        case "push":
            output = push_saves()
            print(output.stdout if output.stdout else output.stderr)
        case "settings":
            open_settings()
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()