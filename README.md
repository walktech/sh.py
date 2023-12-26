# sh.py

This python script makes python scripts into linux batch files known as shell scripts (.sh).

[👨‍💻 Download Python](python.org)

[🖼️ Other Projects](github.com/walktech)

## How do I use it?

Right click and click `Open in Terminal` and put this command in.

```
python start-http.py -e .sh PythonScriptName.py
```

## What about Windows?

No need to worry, follow this.

### 1. Enable WSL and Virtual Machine Platform

Open Powershell as adminstrator and paste both of these commands. **(Restart may be required, maybe. I don't know because I use Linux.)**

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

### 2. Install Ubuntu

Install Ubuntu, the Microsoft Store version and sign up.

### 3. Now you are done.

Type the command to open a sh.

```
./scriptnamehereplease.sh
```
