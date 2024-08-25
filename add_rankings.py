import pandas as pd

def add_rankings(path):
    data = pd.read_csv(path)

    # 2017 season
    data.loc[data["season_team_id"] == "E2016_BAM", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2016_BAR", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2016_BAS", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2016_CSK", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2016_DAR", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2016_GAL", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2016_IST", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2016_MAD", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2016_MIL", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2016_OLY", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2016_PAN", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2016_RED", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2016_TEL", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2016_ULK", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2016_UNK", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2016_ZAL", "ranking"] = 10

    #2018 season
    data.loc[data["season_team_id"] == "E2017_BAM", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2017_BAR", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2017_BAS", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2017_CSK", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2017_KHI", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2017_VAL", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2017_IST", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2017_MAD", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2017_MIL", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2017_OLY", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2017_PAN", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2017_RED", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2017_TEL", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2017_ULK", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2017_MAL", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2017_ZAL", "ranking"] = 4

    #2019 season
    data.loc[data["season_team_id"] == "E2018_MUN", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2018_BAR", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2018_BAS", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2018_CSK", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2018_KHI", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2018_CAN", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2018_IST", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2018_MAD", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2018_MIL", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2018_OLY", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2018_PAN", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2018_BUD", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2018_TEL", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2018_ULK", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2018_DAR", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2018_ZAL", "ranking"] = 9

    #2020 season
    data.loc[data["season_team_id"] == "E2019_MUN", "ranking"] = 18
    data.loc[data["season_team_id"] == "E2019_BAR", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2019_BAS", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2019_CSK", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2019_KHI", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2019_PAM", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2019_IST", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2019_MAD", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2019_MIL", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2019_OLY", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2019_PAN", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2019_RED", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2019_TEL", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2019_ULK", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2019_ASV", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2019_ZAL", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2019_DYR", "ranking"] = 17
    data.loc[data["season_team_id"] == "E2019_BER", "ranking"] = 16

    #2021 season
    data.loc[data["season_team_id"] == "E2020_MUN", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2020_BAR", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2020_BAS", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2020_CSK", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2020_KHI", "ranking"] = 18
    data.loc[data["season_team_id"] == "E2020_PAM", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2020_IST", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2020_MAD", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2020_MIL", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2020_OLY", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2020_PAN", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2020_RED", "ranking"] = 17
    data.loc[data["season_team_id"] == "E2020_TEL", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2020_ULK", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2020_ASV", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2020_ZAL", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2020_DYR", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2020_BER", "ranking"] = 15

    #2022 season
    data.loc[data["season_team_id"] == "E2021_MUN", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2021_BAR", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2021_BAS", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2021_CSK", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2021_UNK", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2021_MCO", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2021_IST", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2021_MAD", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2021_MIL", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2021_OLY", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2021_PAN", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2021_RED", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2021_TEL", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2021_ULK", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2021_ASV", "ranking"] = 17
    data.loc[data["season_team_id"] == "E2021_ZAL", "ranking"] = 18
    data.loc[data["season_team_id"] == "E2021_DYR", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2021_BER", "ranking"] = 14

    #2023 season
    data.loc[data["season_team_id"] == "E2022_MUN", "ranking"] = 16
    data.loc[data["season_team_id"] == "E2022_BAR", "ranking"] = 3
    data.loc[data["season_team_id"] == "E2022_BAS", "ranking"] = 8
    data.loc[data["season_team_id"] == "E2022_PAR", "ranking"] = 6
    data.loc[data["season_team_id"] == "E2022_VIR", "ranking"] = 14
    data.loc[data["season_team_id"] == "E2022_MCO", "ranking"] = 4
    data.loc[data["season_team_id"] == "E2022_IST", "ranking"] = 10
    data.loc[data["season_team_id"] == "E2022_MAD", "ranking"] = 2
    data.loc[data["season_team_id"] == "E2022_MIL", "ranking"] = 12
    data.loc[data["season_team_id"] == "E2022_OLY", "ranking"] = 1
    data.loc[data["season_team_id"] == "E2022_PAN", "ranking"] = 15
    data.loc[data["season_team_id"] == "E2022_RED", "ranking"] = 11
    data.loc[data["season_team_id"] == "E2022_TEL", "ranking"] = 5
    data.loc[data["season_team_id"] == "E2022_ULK", "ranking"] = 7
    data.loc[data["season_team_id"] == "E2022_ASV", "ranking"] = 18
    data.loc[data["season_team_id"] == "E2022_ZAL", "ranking"] = 9
    data.loc[data["season_team_id"] == "E2022_PAM", "ranking"] = 13
    data.loc[data["season_team_id"] == "E2022_BER", "ranking"] = 17