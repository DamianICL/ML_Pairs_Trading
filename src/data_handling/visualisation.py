import seaborn as sns
import pandas as pd
from utils.helpers import to_long_data, to_date_time
from utils.config import X_SIZE, Y_SIZE, TITLE_SIZE, LABEL_SIZE, HIGH_RES
import matplotlib.pyplot as plt
import os



def plot_stock_prices(data: pd.DataFrame) -> None:

    # Adjust data from wide to long form
    long_data = to_long_data(data)
    datetime_data = to_date_time(long_data)

    # Configure seaborn
    sns.set_theme(style="whitegrid")
    sns.lineplot(x="Date", y="Price",hue='Stock', data=datetime_data, markers=True, palette='tab10')

    # Label the plot
    plt.figure(figsize=(X_SIZE, Y_SIZE))
    plt.title("Historical Stock Prices (4-Year Time Frame) / Log Scale", fontsize=TITLE_SIZE)
    plt.xlabel("Date", fontsize=LABEL_SIZE)
    plt.ylabel("Adjusted Closing Price", fontsize=LABEL_SIZE)
    plt.legend(title='Stock Ticker', bbox_to_anchor=(1.05, 1), loc='upper left')  # Position the legend outside the plot
    plt.tight_layout()

    # Write to a file in figures
    figures_dir = os.path.join(os.path.dirname(__file__), '../../figures/')
    os.makedirs(figures_dir, exist_ok=True)  # Creates the directory if it doesn't exist
    plot_path = os.path.join(figures_dir, 'historical_stock_prices.png')
    plt.savefig(plot_path, dpi=HIGH_RES, bbox_inches='tight')

    plt.show()




