# em111

This repository contains a Python utility to read Modbus registers from Carlo Gavazzi EM111 energy meter.

# Installation

Clone this repository:

```
git clone https://github.com/hubpav/em111.git
```

Go to the Git repository:

```
cd em111
```

Create Python virtual environment:

```
python -m venv .venv
```

Activate Python virtual environment:

```
source .venv/bin/activate
```

> Note: On Windows in PowerShell, this command will be: `.venv\Scripts\Activate.ps1`

Install all dependencies:

```
pip install -r requirements.txt
```

# Usage

```
python -m em111 --port /dev/ttyUSB0
```

Example output:

```
Voltage: 239.8 V
Current: 0.0 A
Power: 0.0 W
Power factor: 0.0
Frequency: 50.0 Hz
Total power import: 0.0 kWh
Total power export: 0.0 kWh
```
