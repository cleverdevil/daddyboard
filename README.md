# Daddyboard

This repository contains the code for the web service portion of my 
[digital status board project](https://cleverdevil.io/2020/hey-siri-dont-bother-daddy).
It is an extremely simple web service implemented in Python, along with a very
basic web interface that can be loaded on any web browser, including a tablet
like I use to mount on my home office door.

## Installation

I recommend installing this project into a Python 3.7 or higher `virtualenv`.
First, clone this repository, and from within the project directory:

```
virtualenv venv
. venv/bin/activate
pip install -e .
```

This will create the virtual environment, activate it, and then install the
project in-place. From here, you can run the service:

```
pecan serve config.py
```

By default, the service will run on `0.0.0.0` on port `9321` in debug mode. For
more information on how to deploy the service in a more "production" friendly
way, please refer to [the pecanpy documentation](https://pecan.readthedocs.io/en/latest/deployment.html).

## Usage

To view the user-friendly current status page:

`http://your-ip-address:9321/view.html`

To see the current status in JSON format:

`http://your-ip-address:9321/`

To set a new status, send one of the three following requests:

* `http://your-ip-address:9321/set_state/AVAILABLE`
* `http://your-ip-address:9321/set_state/QUIET_PLEASE`
* `http://your-ip-address:9321/set_state/DO_NOT_DISTURB`

To check if the current status is specifically one of the three statuses above:

* `http://your-ip-address:9321/is_state/AVAILABLE`
* `http://your-ip-address:9321/is_state/QUIET_PLEASE`
* `http://your-ip-address:9321/is_state/DO_NOT_DISTURB`

I recommend using a cheap Android tablet for your status board, and installing a
"full screen" web browser (there are many available for free) and an app that
lets you force the tablet not to put its screen to sleep.

## Homebridge Integration

Integrating your status board with Apple HomeKit requires the use of the
excellent [Homebridge](https://homebridge.io) project. Once you have Homebridge
installed and configured, you can use the [HTTP Switch Plugin](https://github.com/Supereg/homebridge-http-switch)
to integrate your status board. Here is an excerpt from my configuration:

```
"accessories": [
    {
        "accessory": "HTTP-SWITCH",
        "name": "DaddyIsAvailable",
        "switchType": "stateful",
        "onUrl": "http://127.0.0.1:9321/set_state/AVAILABLE",
        "offUrl": "http://127.0.0.1:9321/set_state/AVAILABLE",
        "statusUrl": "http://127.0.0.1:9321/is_state/AVAILABLE",
        "pullInterval": 500
    },
    {
        "accessory": "HTTP-SWITCH",
        "name": "DaddyNeedsQuiet",
        "switchType": "stateful",
        "onUrl": "http://127.0.0.1:9321/set_state/QUIET_PLEASE",
        "offUrl": "http://127.0.0.1:9321/set_state/AVAILABLE",
        "statusUrl": "http://127.0.0.1:9321/is_state/QUIET_PLEASE",
        "pullInterval": 500
    },
    {
        "accessory": "HTTP-SWITCH",
        "name": "DontBotherDaddy",
        "switchType": "stateful",
        "onUrl": "http://127.0.0.1:9321/set_state/DO_NOT_DISTURB",
        "offUrl": "http://127.0.0.1:9321/set_state/AVAILABLE",
        "statusUrl": "http://127.0.0.1:9321/is_state/DO_NOT_DISTURB",
        "pullInterval": 500
    }
]
```

In my configuration, I have defined three "stateful" switches that can be
toggled on and off, and impact one another. The switches can be added to scenes,
used in shortcuts, and more.
