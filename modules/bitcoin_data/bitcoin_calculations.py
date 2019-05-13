def calculate_subsidy_era(current_blockheight):
    # scheme {era : [era, subsidy reward, min_blockheight]}
    # see https://en.bitcoin.it/wiki/Controlled_supply for more info

    subsidy_era = {1: [1, 50, 0],
                   2: [2, 25, 21000],
                   3: [3, 12.5, 420000],
                   4: [4, 6.25, 630000],
                   5: [5, 3.125, 840000],
                   6: [6, 1.56250000, 1050000],
                   7: [7, 0.78125000, 1260000],
                   8: [8, 0.39062500, 1470000],
                   9: [9, 0.19531250, 1680000],
                   10: [10, 0.09765625, 1890000],
                   11: [11, 0.04882812, 2100000],
                   12: [12, 0.02441406, 2310000],
                   13: [13, 0.01220703, 2520000],
                   14: [14, 0.00610351, 2730000],
                   15: [15, 0.00305175, 2940000],
                   16: [16, 0.00152587, 3150000],
                   17: [17, 0.00076293, 3360000],
                   18: [18, 0.00038146, 3570000],
                   19: [19, 0.00019073, 3780000],
                   20: [20, 0.00009536, 3990000],
                   21: [21, 0.00004768, 4200000],
                   22: [22, 0.00002384, 4410000],
                   23: [23, 0.00001192, 4620000],
                   24: [24, 0.00000596, 4830000],
                   25: [25, 0.00000298, 5040000],
                   26: [26, 0.00000149, 5250000],
                   27: [27, 0.00000074, 5460000],
                   28: [28, 0.00000037, 5670000],
                   29: [29, 0.00000018, 5880000],
                   30: [30, 0.00000009, 6090000],
                   31: [31, 0.00000004, 6300000],
                   32: [32, 0.00000002, 6510000],
                   33: [33, 0.00000001, 6720000],
                   34: [34, 0.00000000, 6930000]}

    for key, value in subsidy_era.items():
        if current_blockheight < value[2]:
            return subsidy_era[key - 1]

    return []


def count_blocks_until_next_subsidy_era(current_blockheight, min_blockheight_next_era):
    return min_blockheight_next_era - current_blockheight


def count_aproximate_days_until_next_subsidy_era(blocks_until_new_era):
    return round(blocks_until_new_era / 144)


def calculate_percentage_of_blocks_until_next_subsidy_era(current_blockheight, min_blockheight_next_era):
    pevious_min_blockheight_era = min_blockheight_next_era - 210000
    return str(round((pevious_min_blockheight_era / current_blockheight) * 100))
