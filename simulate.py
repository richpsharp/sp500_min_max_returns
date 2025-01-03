import os
import pandas
from concurrent.futures import ProcessPoolExecutor

import pandas as pd

def calculate_signed_momentum(df, window=10):
    df = df.sort_values(by='Date')
    df['Price_ROC'] = df['Close'].diff(window - 1) / df['Close'].shift(window - 1)
    df['Volume_MA'] = df['Volume'].rolling(window=window).mean()
    df['Momentum'] = df['Price_ROC'] * df['Volume_MA']
    df.drop(['Price_ROC', 'Volume_MA'], axis=1, inplace=True)
    return df


def plot_price_and_other(df, axis_a, axis_b):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df['Date'], df[axis_a], label=axis_a, color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel(axis_a, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2 = ax1.twinx()
    ax2.plot(df['Date'], df[axis_b], label=axis_b, color='orange')
    ax2.set_ylabel(axis_b, color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    plt.title('Stock Price and Momentum Over Time')
    fig.tight_layout()
    plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)

    plt.show()



def simulate_trading(df, initial_cash=1000):
    cash = initial_cash
    stock_owned = 0
    transactions = []  # To store transaction details

    for index, row in df.iterrows():
        current_momentum = row['Momentum']
        current_price = row['Close']

        if current_momentum > 0 and stock_owned == 0:
            stock_owned = cash / current_price
            cash = 0
            transactions.append((row['Date'], 'Buy', current_price, current_momentum, cash, cash+stock_owned*current_price-initial_cash))
        elif stock_owned > 0 and current_momentum < 0:
            cash = stock_owned * current_price
            stock_owned = 0
            transactions.append((row['Date'], 'Sell', current_price, current_momentum, cash, cash+stock_owned*current_price-initial_cash))
        else:
            transactions.append((row['Date'], 'Hold', current_price, current_momentum, cash, cash+stock_owned*current_price-initial_cash))

    if stock_owned > 0:
        cash = stock_owned * df.iloc[-1]['Close']

    results = pd.DataFrame(transactions, columns=['Date', 'Action', 'Price', 'Momentum', 'Cash', 'Return'])
    return results, cash-initial_cash

def process_all_stocks(stocks, window=60, initial_cash=1000):
    results = []
    total_return = 0

    for stock_name, df in stocks.items():
        print(f'calculating signed momentum for {stock_name} and {window}')
        df_with_signed_momentum = calculate_signed_momentum(df, window=window)
        print(f'simulating trading for {stock_name} and {window}')
        _, final_return = simulate_trading(df_with_signed_momentum, initial_cash=initial_cash/len(stocks))
        results.append({'Stock': stock_name, 'Final Return': final_return})
        total_return += final_return

    # Create a results DataFrame
    results_df = pd.DataFrame(results)
    results_df.sort_values(by='Final Return', ascending=False, inplace=True)

    return results_df, total_return


def process_window(window, stocks):
    print(f'Simulating window range {window}')
    stock_results, total_returns = process_all_stocks(stocks, window=window, initial_cash=1000)
    print(f'Done simulating window range {window}, accumulating to df')
    # Add a 'Total Return' row
    stock_results = pd.concat(
        [pd.DataFrame({'Stock': ['Total Return'], 'Final Return': [total_returns]}), stock_results],
        ignore_index=True
    )

    print(f'Returning result of {window}')
    return window, stock_results.set_index('Stock')['Final Return']


def plot_total_return_vs_window(summary_df):
    """
    Plot a scatterplot of Total Return vs. Window Size.

    :param summary_df: DataFrame where each row is a window size, and the first column is 'Total Return'.
    """
    # Extract Total Return values and window sizes
    summary_df = summary_df.T  # Ensure the DataFrame is transposed correctly
    total_returns = summary_df.loc['Total Return']
    window_sizes = total_returns.index.astype(int)

    # Create the scatter plot
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.scatter(window_sizes, total_returns, color='blue', alpha=0.7, edgecolors='k')
    plt.title('Total Return vs. Window Size')
    plt.xlabel('Window Size')
    plt.ylabel('Total Return')
    plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()


def main():
    """Entry point."""

    # Run the processing for all stocks
    print('reading all the stock files')
    raw_directory = './raw'
    files = [os.path.join(raw_directory, filename) for filename in os.listdir(raw_directory) if filename.endswith('.csv')]
    stocks = {}
    for filepath in files:
        df = pd.read_csv(filepath)
        stocks[os.path.basename(os.path.splitext(filepath)[0])] = df
    print('ready to simulate')
    results = {}  # Dictionary to store results for each window size
    window_range = range(15, 25)  # Define the window range

    with ProcessPoolExecutor(6) as executor:
        # Map each window to a parallel process
        futures = executor.map(process_window, window_range, [stocks] * len(window_range))

    # Collect results
    for window, result in futures:
        results[window] = result

    # Combine results into a single DataFrame
    summary_df = pd.DataFrame(results)

    # Transpose and sort for better readability
    summary_df = summary_df.T
    summary_df = summary_df[['Total Return'] + [col for col in summary_df.columns if col != 'Total Return']]
    summary_df = summary_df.T
    summary_df.to_csv('report.csv')

    plot_total_return_vs_window(summary_df.T)


if __name__ == '__main__':
    main()
