# BitcoinDataTwitterBot

The goal of the project is to provide a small twitter bot written in Python that tweets out whenever a percentual change to the next halving happens. In additon to that it should tweet out a random quote of satoshi each day(WIP).

## Getting Started

It is required to follow the instructions of /resource/api_keys_example and insert your Twitter Developer Account API keys there. Also rename the file to api_keys.txt and save it at the same directory.

To get the bot running start the tweet_scheduler.py or a binary file that might be released later on. From there on the bot is running on its own and checks every day at 12:00 if the halving has came a % closer and will tweet this out.

In the directory /venv/ a full preinstalled version of Python 3.7 and all containing libraries of this project is ready to be used for Windows machines. Linux need to foolow the Prerequisites section.

### Prerequisites

Please install

* Python 3.7
* Schedule (pip install schedule)
* Tweepy (pip install tweepy)

### Installing

A step by step series of examples that tell you how to get a venv running

```
For Linux:
sudo apt install python3.7
pip install schedule
pip install tweepy

For Windows to use the venv environment:
(Navigate to the project directory)
venv/Scripts/activate
cd ..
cd ..
python tweet_scheduler.py
```

When you see the string "running" in the terminal the scheduler is waiting for the Bitcoin network to progress and reach the threshold to tweet the progress out.

## Versioning

version 0.1

## Authors

* **Sascha Majewsky**