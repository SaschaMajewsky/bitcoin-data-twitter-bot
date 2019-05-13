import schedule
import time
from modules.fileIO.persist_tweet import persist_tweet_in_file
from modules.twitter.tweet import send_tweet
from modules.twitter.tweet_generation import generate_tweet_bitcoin_halving_progression
from modules.bitcoin_data.bitcoin_api_data import get_btc_current_blockheight
from modules.bitcoin_data.bitcoin_calculations import calculate_subsidy_era, count_blocks_until_next_subsidy_era,\
    calculate_percentage_of_blocks_until_next_subsidy_era, count_aproximate_days_until_next_subsidy_era


def job():
    btc_current_blockheight = get_btc_current_blockheight()
    subsidy_era = calculate_subsidy_era(btc_current_blockheight)
    blocks_until_next_subsidy_era = count_blocks_until_next_subsidy_era(btc_current_blockheight, subsidy_era[2])
    aproximate_days_until_next_subsidy_era = count_aproximate_days_until_next_subsidy_era(blocks_until_next_subsidy_era)
    percentage_of_blocks_until_next_subsidy_era =\
        calculate_percentage_of_blocks_until_next_subsidy_era(btc_current_blockheight, subsidy_era[2])
    print(btc_current_blockheight)
    
    if 'there is new file':
        tweet = generate_tweet_bitcoin_halving_progression(3, 12.5, 54246, 377, 72.95)
        send_tweet(tweet)
        persist_tweet_in_file(72.95, "last_halving_tweet.txt")


schedule.every().day.at("15:28").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
