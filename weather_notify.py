#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests

def fetch_weather(api_key: str, city: str) -> dict:
    """
    OpenWeatherMap から天気情報を取得する
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric", "lang": "ja"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

def make_suggestion(weather: dict) -> str:
    """
    weather['weather'][0]['main'] や weather['weather'][0]['description'] から
    シンプルな行動提案文を返す
    """
    main = weather["weather"][0]["main"].lower()
    desc = weather["weather"][0]["description"]

    if "rain" in main or "雨" in desc:
        return "今日は雨が降っています。傘をお持ちください☔️"
    elif "clear" in main or "晴" in desc:
        return "快晴です。外でリフレッシュすると良いでしょう🌞"
    elif "cloud" in main or "曇" in desc:
        return "曇り空です。念のため軽い上着があると安心です☁️"
    elif "snow" in main or "雪" in desc:
        return "雪の予報です。足元にご注意ください❄️"
    else:
        return "天気情報を確認の上、適宜ご準備をお願いします☀️"

def post_to_slack(webhook_url: str, message: str):
    """
    Slack Incoming Webhook にメッセージを投げる
    """
    payload = {"text": message}
    resp = requests.post(webhook_url, json=payload)
    resp.raise_for_status()

def main():
    # 環境変数から情報を取得
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = os.getenv("CITY_NAME", "Tokyo,JP")
    webhook = os.getenv("SLACK_WEBHOOK_URL")

    if not (api_key and webhook):
        print("Error: OPENWEATHER_API_KEY と SLACK_WEBHOOK_URL を環境変数で設定してください。", file=sys.stderr)
        sys.exit(1)

    # 1. 天気取得
    weather = fetch_weather(api_key, city)
    temp = weather["main"]["temp"]
    description = weather["weather"][0]["description"]

    # 2. 行動提案文生成
    suggestion = make_suggestion(weather)

    # 3. Slack へ投稿
    message = (
        f"*{city} の天気速報*\n"
        f"気温：{temp:.1f}℃\n"
        f"天気：{description}\n\n"
        f"💡 *行動提案*: {suggestion}"
    )
    post_to_slack(webhook, message)
    print("Slack への通知が完了しました。")

if __name__ == "__main__":
    main()
