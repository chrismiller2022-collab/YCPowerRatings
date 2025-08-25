import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="College Football Power Rankings",
    page_icon="🏈",
    layout="wide"
)

# Title and header
st.title("🏈 College Football Power Rankings")
st.markdown("---")

# For now, we'll use sample data - later you can replace this with your Google Sheets data
@st.cache_data
def load_sample_data():
    """Load sample power rankings data"""
    data = {
        'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'Team': [
            'Georgia', 'Michigan', 'Texas', 'Alabama', 'Oregon', 
            'Ohio State', 'Penn State', 'Washington', 'Florida State',
            'USC', 'Notre Dame', 'Tennessee', 'LSU', 'Utah', 'Oklahoma'
        ],
        'Record': [
            '12-1', '15-0', '12-2', '12-2', '12-2',
            '11-2', '11-2', '14-1', '13-1', '11-3',
            '10-3', '9-4', '10-4', '10-4', '10-3'
        ],
        'Points': [1456, 1423, 1387, 1345, 1298, 1256, 1189, 1156, 1089, 1034, 987, 934, 876, 823, 789],
        'Previous_Rank': [2, 1, 4, 3, 6, 5, 8, 7, 9, 11, 10, 12, 13, 15, 14],
        'Change': ['↑1', '↓1', '↑1', '↓1', '↑1', '↓1', '↑1', '↓1', '→', '↑1', '↓1', '→', '→', '↑1', '↓1']
    }
    return pd.DataFrame(data)

# Load the data
df = load_sample_data()

# Display last updated info
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Current Rankings")
with col2:
    st.write(f"**Last Updated:** {datetime.now().strftime('%B %d, %Y')}")

# Display the rankings table
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Rank": st.column_config.NumberColumn("Rank", width="small"),
        "Team": st.column_config.TextColumn("Team", width="medium"),
        "Record": st.column_config.TextColumn("Record", width="small"),
        "Points": st.column_config.NumberColumn("Points", width="small"),
        "Previous_Rank": st.column_config.NumberColumn("Prev Rank", width="small"),
        "Change": st.column_config.TextColumn("Change", width="small")
    }
)

# Add some statistics
st.markdown("---")
st.subheader("📊 Quick Stats")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Teams Ranked", len(df))
with col2:
    undefeated = len(df[df['Record'].str.contains('0', regex=False)])
    st.metric("Undefeated Teams", undefeated)
with col3:
    avg_points = df['Points'].mean()
    st.metric("Average Points", f"{avg_points:.0f}")
with col4:
    top_points = df['Points'].iloc[0]
    st.metric("Top Team Points", top_points)

# Sidebar for future features
st.sidebar.title("Navigation")
st.sidebar.markdown("**Current Features:**")
st.sidebar.markdown("- View Power Rankings")
st.sidebar.markdown("- Team Statistics")

st.sidebar.markdown("**Coming Soon:**")
st.sidebar.markdown("- Team Details")
st.sidebar.markdown("- Historical Rankings")
st.sidebar.markdown("- Comparison Tools")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "College Football Power Rankings App | Built with Streamlit"
    "</div>", 
    unsafe_allow_html=True
)
