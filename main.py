"""main module"""
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import polars as pl

def display_highest_votes():
    """
    Display basic info about movies dataset
    """
    polars_movies_df = pl.read_csv("MoviesTopRated.csv")
    polars_vote_df = polars_movies_df.query("vote_average == vote_average.max()")
    print("Summary Statistics of the Top Rated Movies Dataset:\n")
    print(polars_movies_df.describe())
    polars_movies_df.plot.scatter(
        x="popularity",
        y="vote_average",
        title="popularity vs vote_average graph",
        xlabel="Popularity",
        ylabel="Average Ratings out of 10",
    )
    plt.show()
    print("\nDetails of the movies that were given the highest votes are: \n")
    print(polars_vote_df)
    polars_report_generator(polars_movies_df)
    return polars_vote_df


def polars_report_generator(df):
    profile = ProfileReport(df, title="Summary Report")
    profile.to_file("Polars_Summary_Report.html")
