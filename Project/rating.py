import csv
import plotly.figure_factory as pff

with open("D:/(4) WhiteHatJr. Codes/Third Module/Bell Curve/Project/rating.csv", newline = "") as f:
    reader = list(csv.reader(f))
    reader.pop(0)

    rating_list = list()

    for i in range(len(reader)):
        avg_rating = reader[i][2]
        rating_list.append(float(avg_rating))

    figure = pff.create_distplot([rating_list], ["Average Rating"], show_hist =  False)

    figure.show()