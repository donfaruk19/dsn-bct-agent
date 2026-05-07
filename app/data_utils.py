import pandas as pd


def load_and_clean_data(file_path='amazon.csv'):
    df = pd.read_csv(file_path)

    # We only need these for our Agent logic
    core_columns = [
        'user_id', 'user_name', 'product_name',
        'category', 'rating', 'review_content'
    ]
    df = df[core_columns]

    # Cleaning: Remove currency symbols and convert ratings to numeric
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    # Since some user_ids are lists, we'll take the first one for simplicity
    # in this hackathon version
    df['user_id'] = df['user_id'].str.split(',').str[0]

    return df


def get_user_history(df, user_id):
    """Fetches all reviews by a specific user to build their persona."""
    user_data = df[df['user_id'] == user_id]
    history = ""
    for _, row in user_data.iterrows():
        history += f"Product: {row['product_name']} | Rating: {row['rating']} | Review: {row['review_content']}\n"
    return history