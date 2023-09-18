"""main module"""
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import polars as pl

def movies_statistics_polars(movies_csv):
    """
    Display basic info about movies dataset
    """
    # read the .csv dataset into a DataFrame
    polars_movies_df = pl.read_csv(movies_csv)

    # calculate average votes
    max_avg_votes = polars_movies_df["vote_average"].max()
    
    # select rows with the highest average votes
    polars_vote_df = polars_movies_df.filter(pl.col("vote_average") == max_avg_votes)

    # display movies dataset statistics
    print("Summary Statistics of the Top Rated Movies Dataset:\n")
    print(polars_movies_df.describe())

    # generate plot for popularity vs vote_average
    plt.scatter(polars_movies_df["popularity"],polars_movies_df["vote_average"])
    plt.title("popularity vs vote_average graph")
    plt.xlabel("Popularity")
    plt.ylabel("Average Ratings out of 10")
    plt.show()

    print("\nDetails of the movies that were given the highest votes are: \n")
    print(polars_vote_df)
    polars_report_generator()
    return polars_vote_df


def polars_report_generator(movies_csv):
    polars_movies_df = pl.scan_csv(movies_csv)
    profile = ProfileReport(polars_movies_df, title="Summary Report")
    profile.to_file("Polars_Summary_Report.html")
