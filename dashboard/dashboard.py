import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

day_df['season'] = day_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
hour_df['season'] = hour_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
hour_df['workingday'] = hour_df['workingday'].map({0: 'non-Workingday', 1: 'Workingday'})
day_df['workingday'] = day_df['workingday'].map({0: 'non-Workingday', 1: 'Workingday'})

def visualize_rental_trends_by_day_type(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(data=df, x='workingday', y='cnt', estimator=sum, ax=ax)
    ax.set_xlabel('Day Type')
    ax.set_ylabel('Total Bike Rentals')
    ax.set_title('Difference in Bike Rental Trends between Workingday and non-Workingday')
    st.pyplot(fig)

def visualize_rental_usage_by_season(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='season', y='cnt', showfliers=False, palette='bright', ax=ax)
    ax.set_title(f'Bike Rental Usage in {df["season"].iloc[0]}')
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Bike Rentals')
    st.pyplot(fig)

    total_rentals = df['cnt'].sum()
    st.write(f"Total Bike Rentals in {df['season'].iloc[0]}: {total_rentals}")

def main():
    st.title("Bike Rental Dashboard")

    st.header("Bike Rental Trends by Day Type")
    visualize_rental_trends_by_day_type(hour_df)

    st.header("Bike Rental Usage by Season")
    visualize_rental_usage_by_season(hour_df)

    st.header("Bike Rental Usage by Selected Season")
    selected_season = st.selectbox("Select Season", ["Spring", "Summer", "Fall", "Winter"])
    filtered_df = hour_df[hour_df['season'] == selected_season]
    visualize_rental_usage_by_season(filtered_df)


if __name__ == "__main__":
    main()
