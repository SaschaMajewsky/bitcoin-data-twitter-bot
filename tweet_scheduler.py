import schedule
import time
import os
import random
from packages.fileIO.persist_tweet import persist_tweet_in_file
from packages.twitter.tweet import send_tweet
from packages.twitter.tweet_generation import generate_tweet_bitcoin_halving_progression, generate_tweet_satoshi_quote_of_the_day
from packages.bitcoin_data.bitcoin_api_data import get_btc_current_blockheight
from packages.bitcoin_data.bitcoin_calculations import calculate_subsidy_era, count_blocks_until_next_subsidy_era,\
    calculate_percentage_of_blocks_until_next_subsidy_era, count_aproximate_days_until_next_subsidy_era
from packages.quotes.get_quotes import get_quote_of_satoshi


print('running')


def job_tweet_halving():
    btc_current_blockheight = get_btc_current_blockheight()
    subsidy_era = calculate_subsidy_era(btc_current_blockheight)
    blocks_until_next_subsidy_era = count_blocks_until_next_subsidy_era(btc_current_blockheight,
                                                                        subsidy_era[2])
    aproximate_days_until_next_subsidy_era = count_aproximate_days_until_next_subsidy_era(blocks_until_next_subsidy_era)
    percentage_of_blocks_until_next_subsidy_era =\
        calculate_percentage_of_blocks_until_next_subsidy_era(btc_current_blockheight, subsidy_era[2])

    file = open(os.path.join(os.path.dirname(__file__)) +
                "/resources/last_halving_tweet.txt")
    lines = file.readlines()
    last_percentage_tweeted = lines[0].split("\n")
    file.close()
    print(percentage_of_blocks_until_next_subsidy_era)
    if float(last_percentage_tweeted[0]) < float(percentage_of_blocks_until_next_subsidy_era):
        tweet = generate_tweet_bitcoin_halving_progression(subsidy_era[0], subsidy_era[1],
                                                           blocks_until_next_subsidy_era,
                                                           aproximate_days_until_next_subsidy_era,
                                                           percentage_of_blocks_until_next_subsidy_era)
        send_tweet(tweet)
        persist_tweet_in_file(percentage_of_blocks_until_next_subsidy_era, "last_halving_tweet.txt")


def job_tweet_satoshi_quote_of_the_day():
        max_count_satoshi_quote = 70
        tweet = generate_tweet_satoshi_quote_of_the_day((get_quote_of_satoshi(random.randint(1, max_count_satoshi_quote))))
        send_tweet(tweet)


schedule.every().day.at("03:37").do(job_tweet_halving)
schedule.every().day.at("12:00").do(job_tweet_satoshi_quote_of_the_day)

while 1:
    schedule.run_pending()
    time.sleep(1)
