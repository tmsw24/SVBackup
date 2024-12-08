# Stardew Valley Backup Tool (SVBackup)
A simple tool for backing up and restoring your Stardew Valley saves from an Android device to a Windows PC, and vice versa.

## Features
- A **command-line interface (CLI)**
- A **graphical user interface (GUI)**
- Configurable paths stored in `settings.json`

## Requirements
- A Windows operating system
- Python 3.x is installed
- An Android device with **Developer Options** and **USB Debugging** enabled.

## Usage
### 1. Configure `settings.json`
By default, SVBackup will pull saves to a `backup` folder on your PC (which will be automatically created in the projects directory) and saves will be pushed back to `Documents/SVBackup` on your Android device.

If you want different directories to save to, you can change `mobile-directory` and `computer-directory` in `settings.json`.

### 2. Running the tool
Make sure your Android device has **Developer Options** and **USB Debugging** enabled, and it's connected to your PC via USB.

#### Command-Line Interface (CLI)
Navigate to the projects directory in a terminal and run:

```
python svbackup.py
```

#### Graphical User Interface (GUI)
Navigate to the projects directory a terminal or file explorer and run `svbackupgui.pyw`.

### 3. Pulling / Pushing
#### Pull
Choosing the **pull** option transfers your Stardew Valley saves from your Android device to your PC.

#### Push
Choosing the **push** option transfers your Stardew Valley saves from your PC to your Android device.

## Contributing
Contributions are welcome. Feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.