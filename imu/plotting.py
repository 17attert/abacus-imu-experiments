import csv
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


def plot_distribution(data, key, plot_title, path_to_csv_file=None):
    """
    Gaussian distribution plots
    
    """
    size = len(data)

    # CSV writer
    if path_to_csv_file != None:
        csv_file = open(path_to_csv_file, 'w')
        writer = csv.writer(csv_file)

        # Write header
        writer.writerow([
            key[0]+"_mean", key[0] + "_std", 
            key[1]+"_mean", key[1] + "_std", 
            key[2]+"_mean", key[2] + "_std", 
        ])

    values_for_csv_file = []
    colours = ['tab:blue', 'tab:orange', 'tab:green']
    averages = []
    for i in range(size):
        mu, sigma = data[i].mean(), data[i].std()
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)         
        
        plt.plot(x, stats.norm.pdf(x, mu, sigma), color=colours[i])

        values_for_csv_file.append(mu)
        values_for_csv_file.append(sigma)

        averages.append(mu)
    
    if path_to_csv_file != None:
        # Write mean/std values
        writer.writerow(values_for_csv_file)
        
        # Close the CSV file
        csv_file.close()

    plt.title(plot_title)