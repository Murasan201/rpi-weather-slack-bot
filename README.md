# rpi-weather-slack-bot

A Python script for Raspberry Pi that fetches current weather from OpenWeatherMap and posts actionable suggestions to Slack via Incoming Webhook.

## Features

- Fetches current weather for specified city (default: Tokyo,JP)
- Generates actionable suggestion based on weather condition
- Posts formatted message to Slack channel via Incoming Webhook

## Prerequisites

- Python 3.6 or higher
- `requests` library  
- OpenWeatherMap API key with "Current weather and forecasts" plan enabled

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rpi-weather-slack-bot.git
   cd rpi-weather-slack-bot
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

## Configuration

Set the following environment variables before running the script:

```bash
export OPENWEATHER_API_KEY="your_openweather_api_key"
export CITY_NAME="Tokyo,JP"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/your/webhook/url"
```

## Usage

Run the script manually:

```bash
python weather_notify.py
```

## Scheduling with cron

To run the script automatically every day at 7:00 AM, add a cron entry:

```cron
0 7 * * * /usr/bin/env python3 /path/to/weather_notify.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

[Murasan](https://murasan-net.com/)
