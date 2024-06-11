# Signal Scheduler

This Python script allows you to schedule Signal messages to be sent at specific dates and times. You can send messages to both individual contacts and groups.

## Requirements

- Python 3
- `pytz` library
- `schedule` library
- `signal-cli` installed and configured

## Installation

1. **Install Python 3**

   Make sure you have Python 3 installed on your machine. You can download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**

   Install the required Python libraries using pip:

   ```bash
   pip install pytz schedule
   ```

3. **Install signal-cli**

   Follow the instructions on the [signal-cli GitHub page](https://github.com/AsamK/signal-cli) to install and configure `signal-cli` on your machine.

## Configuration

1. **Set Up Your Phone Number and Contacts**

   Edit the script to replace `+123456789` with your Signal phone number. Also, update the `group1`, `group2`, `person1`, and `person2` variables with the actual IDs and phone numbers.

2. **Schedule Messages**

   Modify the `scheduled_messages` list to include your own scheduled messages. Each message should have the following format:

   ```python
   {'date_time': 'YYYY-MM-DD HH:MM:SS', 'identifier': 'ID_OR_PHONE_NUMBER', 'message': 'YOUR_MESSAGE', 'timezone': 'TIMEZONE', 'is_group': True_or_False}
   ```

   - `date_time`: The date and time when the message should be sent.
   - `identifier`: The ID of the group or the phone number of the individual.
   - `message`: The message you want to send.
   - `timezone`: The timezone in which the date and time are specified.
   - `is_group`: `True` if sending to a group, `False` if sending to an individual.

## Usage

1. **Run the Script**

   Run the script using Python:

   ```bash
   python3 path_to_your_script.py
   ```
2. **Run at Startup**

To run the script automatically at startup, you can create a systemd service.

### Step-by-Step Guide

1. **Find JAVA_HOME and PATH**

   First, find the path to your Java installation. You can do this by running:

   ```bash
   which java
   ```

   Then, find the Java home directory:

   ```bash
   readlink -f $(which java) | sed "s:bin/java::"
   ```

   Note the output, which will be used in the service file.

2. **Create a Systemd Service File**

   Open a terminal and create a new service file. For example, if your script is named `signal-scheduler.py`, create a service file named `signal-scheduler.service`:

   ```bash
   sudo nano /etc/systemd/system/signal-scheduler.service
   ```

3. **Edit the Service File**

   Add the following content to the service file, adjusting the paths and descriptions as necessary:

   ```ini
   [Unit]
   Description=Signal Scheduler Python Script
   After=network.target

   [Service]
   Environment="JAVA_HOME=/opt/jdk-21+35" # Replace with your JAVA_HOME
   Environment="PATH=/opt/jdk-21+35/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" # Replace with your PATH
   ExecStart=/usr/bin/python3 /path/to/signal-scheduler.py # Replace with your path to the python script
   WorkingDirectory=/home/yourworkingdirectory # Replace with your working directory
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=yourusername # Replace with your user name

   [Install]
   WantedBy=multi-user.target
   ```


4. **Reload Systemd Configuration**

   Reload the `systemd` manager configuration to apply the changes:

   ```bash
   sudo systemctl daemon-reload
   ```

5. **Enable the Service to Start on Boot**

   Enable the service so that it starts automatically on boot:

   ```bash
   sudo systemctl enable signal-scheduler.service
   ```

6. **Start the Service**

   Start the service immediately without rebooting:

   ```bash
   sudo systemctl start signal-scheduler.service
   ```

7. **Check the Status of the Service**

   Verify that the service is running and check for any errors:

   ```bash
   sudo systemctl status signal-scheduler.service
   ```
