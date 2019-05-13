from modules.twitter.tweet import send_tweet

def generate_tweet_bitcoin_halving_progression(subsidy_era, block_subsidy, remaining_blocks, remaining_days, percentage_progression):
    return "𝗕𝗜𝗧𝗖𝗢𝗜𝗡 𝗛𝗔𝗟𝗩𝗘𝗡𝗜𝗡𝗚 𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦𝗜𝗢𝗡:\n" + "Subsidy Era: " + str(subsidy_era) + "/34\nBlock Subsidy Reward: " +\
           str(block_subsidy) + " ₿\n" + "Remaining Blocks: " + str(remaining_blocks) + " ⬛" + " \nRemaining Days: " +\
           "~" + str(remaining_days) + " ⌛\n" + "Progression until next Era: " + str(percentage_progression)\
           + " %" + "\n\n" + "More Info:\n" + "https://bit.ly/1pQPBGe"

print(generate_tweet_bitcoin_halving_progression(3, 12.5, 54246, 377, 72.95))

#send_tweet(generate_tweet_bitcoin_halving_progression(3, 12.5, 54246, 377, 72.95))
