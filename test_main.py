"""test_main module"""
import main
movies_csv = "MoviesTopRated.csv"


def test_main():
    """
    testing function for main
    """
    polars_highest_votes = main.movies_statistics_polars(movies_csv)
    # print(highest_votes.loc[0,"vote_count"])
    assert polars_highest_votes["vote_count"][0] == 18448
    # print(highest_votes.loc[1,"vote_count"])
    assert polars_highest_votes["vote_count"][1] == 24376


if __name__ == "__main__":
    test_main()
