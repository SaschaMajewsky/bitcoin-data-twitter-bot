def generate_tweet_bitcoin_halving_progression(subsidy_era, block_subsidy, remaining_blocks, remaining_days,
                                               percentage_progression):
    return "𝗕𝗧𝗖 𝗛𝗔𝗟𝗩𝗜𝗡𝗚 𝗜𝗡𝗙𝗢:\n" + "Subsidy Era: " + str(subsidy_era) + "/34\nBlock Subsidy Reward: " +\
           str(block_subsidy) + " ₿\n" + "Progression until next Era: " + str(percentage_progression)\
           + " %" + "\nRemaining: Blocks " + str(remaining_blocks) + " ⬜" + " Days " +\
           "~" + str(remaining_days) + " ⌛\n" + generate_ascii_progress_bar(percentage_progression) +\
           "\nInfo:\n" + "https://bit.ly/1pQPBGe"


def generate_ascii_progress_bar(percentage_given):
    filled_bar_length = int(round(26 * percentage_given / float(100)))
    return '▓' * filled_bar_length + '░' * (26 - filled_bar_length)
