import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
# full width
st.set_page_config(layout="wide")
st.markdown(
        """

        
        <style>


        [data-testid="stSidebar"] {
                background-image: url(https://raw.githubusercontent.com/FareedKhan-dev/iba-logo/main/pngwing.com.png);
                background-size: 200px;
                background-repeat: no-repeat;
                background-position: 4px 20px;
            }

@font-face {
  font-family: 'Inter';

@import url('https://github.com/gattadesmond/hugo-foundation6/blob/master/src/assets/fonts/sf-pro/SF-Pro-Display/sf-pro-display_bold.woff2');
}

    html, body, [class*="css"]  {
    font-family: 'SF Pro Display Regular';
    }
      .main {
        max-width: 100%;
    }
    .custom-title {
        font-size: 40px;
        font-family: 'SF Pro Display Regular';
        font-weight: bold;
        color: #700F1A;
        # background-color: #F8F8F8;
        # padding: 20px;
    }
    .reduce-me {
    width: 70%;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )


# Streamlit UI with side-by-side pie charts
# Render the title with the custom style
st.markdown("<p class='custom-title'>IBA Student Insights - Analytical Report</p><p class='reduce-me'>This report examines and presents an in-depth analysis of the IBA testing database. It includes information about students who have applied to IBA and details about those who are currently enrolled in IBA's bachelor or master programs. The report also visualizes this information to provide a clear understanding.</p>", unsafe_allow_html=True)
st.markdown("Created by <a href='https://www.linkedin.com/in/fareed-khan-dev'>Fareed Hassan Khan</a>", unsafe_allow_html=True)



st.markdown("""---""")


# Sample data (replace this with your actual data)
data = {
    'Science': [
        [505, 360, 426, 1005, 2599, 2642, 2366],
        [121, 70, 74, 173, 415, 491, 148],
        [27, 29, 20, 38, 134, 82, 70]
    ],
    'Engineering': [
        [274, 275, 196, 145, 492, 699, 1023],
        [113, 126, 92, 46, 112, 186, 139],
        [64, 53, 39, 17, 20, 37, 32]
    ],
    'Commerce': [
        [41, 28, 36, 45, 92, 184, 354],
        [32, 27, 33, 32, 49, 71, 95],
        [28, 22, 14, 7, 23, 36, 33]
    ],
    'Medical': [
        [109, 110, 143, 212, 517, 873, 767],
        [41, 44, 40, 19, 71, 128, 61],
        [12, 21, 14, 12, 11, 29, 38]
    ],
    'Other': [
        [13, 4, 11, 22, 49, 34, 46],
        [4, 6, 9, 5, 9, 12, 10],
        [3, 2, 6, 4, 3, 9, 8]
    ],
    'General': [
        [10, 11, 8, 19, 52, 55, 82],
        [3, 2, 3, 14, 20, 29, 18],
        [4, 2, 3, 1, 8, 10, 8]
    ],
    'Others': [
        [3, 3, 2, 3, 2, 7, 37],
        [2, 2, 0, 1, 6, 7, 4],
        [8, 1, 0, 0, 1, 3, 3]
    ]
}


# Add sidebar
st.sidebar.title("\n")

# Define custom color palettes for each chart
custom_color_palette1 = ['#7E7FD7', '#6F72C1', '#6067AB', '#515C95', '#424180', '#33366A', '#1E1E3D']


custom_color_palette2 = ['#3A0066', '#6D33A0', '#9A9AE3', '#7E7FD7', '#B2B2DE', '#C8C8EB', '#B9BAC0']

# Data for the first donut chart
job_categories = ['Management and Leadership', 'Technical and Engineering', 'Sales and Marketing', 'Financial and Accounting', 'Support and Operations', 'Technology and IT', 'Education and Healthcare']
job_counts = [3742, 2190, 2311, 2308, 2578, 1378, 921]

# Create a DataFrame for the first donut chart
data0 = {'Job Category': job_categories, 'Job Count': job_counts}
df0 = pd.DataFrame(data0)

# Create an interactive donut chart using Plotly Express
fig1 = px.pie(df0, values='Job Count', names='Job Category', hole=0.6, color_discrete_sequence=custom_color_palette1)  

# Adjust layout parameters for the first donut chart
fig1.update_layout(
    margin=dict(t=50, b=0, l=0, r=0),  # Adjust top margin for title
    legend=dict(x=1.1, y=0.5),  # Move legend outside the donut chart
    font=dict(size=20)  # Increase label font size
)

# Data for the second donut chart
edu_categories = ['Science', 'Engineering', 'Commerce', 'Medical', 'Other', 'General', 'Others']
edu_counts = [26694, 20495, 16265, 9091, 2902, 2553, 1778]

# Create a DataFrame for the second donut chart
edu_data = {'Education Category': edu_categories, 'Education Count': edu_counts}
edu_df = pd.DataFrame(edu_data)

# Create an interactive donut chart for education using Plotly Express
fig2 = px.pie(edu_df, values='Education Count', names='Education Category', hole=0.6, color_discrete_sequence=custom_color_palette2)  

# Adjust layout parameters for the second donut chart
fig2.update_layout(
    margin=dict(t=50, b=0, l=0, r=0),  # Adjust top margin for title
    legend=dict(x=1.1, y=0.5),  # Move legend outside the donut chart
    font=dict(size=20)  # Increase label font size
)

# Streamlit UI with side-by-side donut charts
st.title('Demographic Distribution of Applicants')

# Create a layout with two columns
col1, col23 = st.columns(2)
# col23.markdown('<style>div { border-right: 2px solid black; }</style>', unsafe_allow_html=True)
# Display the first donut chart in the first column
with col1:
    st.write("This pie chart illustrates the diversity of applicants for the master's program based on their varying levels of job experience. It provides a visual breakdown of the applicant pool, showcasing the distribution of candidates with different work backgrounds.")
    st.plotly_chart(fig1, use_container_width=True)

# Display the second donut chart in the second column
with col23:
    st.write("This chart is about where people applying for the bachelor's program are coming from. It tells us the different types of places and experiences they have, giving us a picture of the diverse group of students interested in the undergraduate program.")
    st.plotly_chart(fig2, use_container_width=True)

###########################################################################################
st.markdown("""---""")



# Sidebar for selecting education category
selected_category = st.sidebar.selectbox('Select Education Category', list(data.keys()))

# Set up the layout with two columns
col1, col2 = st.columns([2, 1])  # Adjust the width ratios as needed

# Line graph using Plotly (in the left column)
# with col1:
st.title('Yearly Distribution of Students Grades')

st.write("This line plot provides an annual overview of student performance across various backgrounds, depicting the total count of grades achieved in categories A, B, and C. By analyzing the trend over the years, it offers insights into how students from different backgrounds are faring academically and whether there are any shifts in grade distributions. This visualization enables a quick understanding of the academic progress within each background group.")

st.write(f"Education Category: {selected_category}")


# Create a DataFrame for the selected category's data
# df_selected = pd.DataFrame(data[selected_category], index=['A', 'B', 'C'], columns=[str(i) for i in range(2015, 2022)])

# Create a DataFrame for the selected category's data
df_selected = pd.DataFrame(data[selected_category], index=['A', 'B', 'C'], columns=[str(i) for i in range(2015, 2022)])

# Create a Plotly figure
fig = go.Figure()

# Add scatter traces for each grade
for grade in df_selected.index:
    fig.add_trace(go.Scatter(x=df_selected.columns, y=df_selected.loc[grade], mode='lines+markers', name=grade, line=dict(width=3)))  # Adjust the width value

# Update layout to customize the appearance
fig.update_layout(
    # title="Education Data",
    xaxis_title="Year",
    yaxis_title="Value",
    legend_title="Grades",
)

# Display the figure using Streamlit
st.plotly_chart(fig, use_container_width=True)

# Text column (in the right column)
# with col2:
    # st.markdown('<br><br>',unsafe_allow_html=True)
    # extra spaces in streamlit

# Display the Matplotlib figure using Streamlit's pyplot support
# st.pyplot(fig)



###########################################################################################
st.markdown("""---""")

# Sample DataFrame
data = {
    'admission_type': ['Direct BBA', 'Direct Accounting & Finance', 'Direct Computer Science',
                        'Direct Economics & Mathematics', 'Direct Economics', 'Direct Social Sciences',
                        'Direct Mathematics', 'Interview BBA', 'Interview Accounting & Finance',
                        'Interview Computer Science', 'Interview Economics & Mathematics',
                        'Interview Economics', 'Interview Social Sciences', 'Interview Mathematics'],
    'program': ['BBA', 'BS (Accounting & Finance)', 'BS (Computer Science)', 'BS (Economics & Mathematics)',
                'BS (Economics)', 'BS (Social Sciences)', 'BS Mathematics', 'BBA', 'BS (Accounting & Finance)',
                'BS (Computer Science)', 'BS (Economics & Mathematics)', 'BS (Economics)', 'BS (Social Sciences)',
                'BS Mathematics'],
    'count': [987, 686, 424, 83, 181, 137, 7, 1391, 788, 612, 125, 248, 149, 9]
}

df = pd.DataFrame(data)

# Normalize counts
df['normalized_count'] = (df['count'] / df.groupby('program')['count'].transform('sum'))*100

# Streamlit UI
st.title("Bachelor Students - Selection Process")

# Sidebar for program selection
selected_program = st.sidebar.selectbox("Select Program", df['program'].unique())

# Filtered data for the selected program
filtered_df = df[df['program'] == selected_program]

# Create grouped histogram for all programs
fig_all_programs = px.bar(df, x='program', y='normalized_count', color='admission_type',
                          labels={'program': 'Program', 'normalized_count': 'Normalized Count'})

# Create histogram for the selected program
fig_selected_program = px.bar(filtered_df, x='admission_type', y='normalized_count', color='admission_type',
                              labels={'admission_type': 'Admission Type', 'normalized_count': 'Normalized Count'})

# Display both histograms side by side
col1, col2 = st.columns((3,2))

with col1:
    st.write(" This analysis examines the caliber of students entering each program by considering various factors such as academic achievements, background diversity, and admission selectivity. Understanding the distribution of student quality provides insights into the appeal and reputation of different programs within the institution.")
    st.plotly_chart(fig_all_programs)

with col2:
    st.write("This graph focuses on presenting the assessment of student quality for each program separately, making it easier to read and understand.")
    st.plotly_chart(fig_selected_program, use_container_width=True)

###################################################################################################
st.markdown("""---""")

# Data
programs = [
    "BBA",
    "BS (Accounting & Finance)",
    "BS (Computer Science)",
    "BS (Economics & Mathematics)",
    "BS (Economics)",
    "BS (Social Sciences)",
    "BS Mathematics",
    "MBA Evening",
    "MBA Executive",
    "MBA Morning",
    "MS (Computer Science)",
    "MS (Economics)",
    "MS (Islamic Banking & Finance)",
    "MS (Marketing)",
    "MS (Mathematics)",
    "MS - Data Sciences",
    "MS - Development Studies",
    "MS - Finance",
    "MS - Management (Full Time)",
    "MS - Management (Part-Time)"
]

accept_counts_bachelor = [420, 394, 233, 119, 200, 199, 65]
reject_counts_bachelor = [423, 275, 235, 102, 271, 245, 96]

accept_counts_master = [51, 191, 49, 63, 55, 24, 8, 7, 90, 33, 28, 22, 15]
reject_counts_master = [45, 95, 43, 2, 15, 13, 20, 6, 6, 13, 10, 28, 17]

# Sidebar selection
program_type = st.sidebar.selectbox("Select Program Type", ["Bachelor", "Master"])


st.title('Program Acceptance vs. Rejection')
st.write("Two graphs that show how students are being accepted into different programs. The first graph combines the acceptance and rejection rates for bachelor's and master's programs, giving us a big picture view. The second graph zooms in and shows the acceptance details for each individual program in both categories. This makes it easier for us to understand which programs students are getting into and helps us see any patterns or trends.")
# Create bar chart based on selection
if program_type == "Bachelor":
    bachelor_accepts = sum(accept_counts_bachelor)
    bachelor_rejects = sum(reject_counts_bachelor)
    bachelor_accept_ratio = bachelor_accepts / (bachelor_accepts + bachelor_rejects)
    bachelor_reject_ratio = bachelor_rejects / (bachelor_accepts + bachelor_rejects)

    fig_bachelor = go.Figure()
    fig_bachelor.add_trace(go.Bar(
        x=['Accept Ratio', 'Reject Ratio'],
        y=[bachelor_accept_ratio, bachelor_reject_ratio],
        name='Bachelor',
        marker_color=['#89CFF0', '#FF4B4B']
    ))
    fig_bachelor.update_layout()

    fig_programs = go.Figure()
    fig_programs.add_trace(go.Bar(
        x=programs[:7],
        y=accept_counts_bachelor,
        name='Accepts',
        marker_color='#89CFF0'
    ))
    fig_programs.add_trace(go.Bar(
        x=programs[:7],
        y=reject_counts_bachelor,
        name='Rejects',
        marker_color='#FF4B4B'
    ))
    fig_programs.update_layout()

    col1, col2 = st.columns((3,8))

    with col1:
        st.plotly_chart(fig_bachelor, use_container_width=True)

    with col2:
        st.plotly_chart(fig_programs, use_container_width=True)

else:
    master_accepts = sum(accept_counts_master)
    master_rejects = sum(reject_counts_master)
    master_accept_ratio = master_accepts / (master_accepts + master_rejects)
    master_reject_ratio = master_rejects / (master_accepts + master_rejects)

    fig_master = go.Figure()
    fig_master.add_trace(go.Bar(
        x=['Accept Ratio', 'Reject Ratio'],
        y=[master_accept_ratio, master_reject_ratio],
        name='Master',
        marker_color=['#89CFF0', '#FF4B4B']
    ))
    fig_master.update_layout(title='Master Accept and Reject Ratios')

    fig_programs = go.Figure()
    fig_programs.add_trace(go.Bar(
        x=programs[7:],
        y=accept_counts_master,
        name='Accepts',
        marker_color='#89CFF0'
    ))
    fig_programs.add_trace(go.Bar(
        x=programs[7:],
        y=reject_counts_master,
        name='Rejects',
        marker_color='#FF4B4B'
    ))
    fig_programs.update_layout()

    col1, col2 = st.columns((3,8))


    with col1:
        st.plotly_chart(fig_master, use_container_width=True)

    with col2:
        st.plotly_chart(fig_programs, use_container_width=True)


###################################################################################################
st.markdown("""---""")


# Streamlit app
st.title("Personal Statement Quality for Programs")

# Sample data for bachelor programs
bachelor_data = [
   {
        "Program": "BBA",
        "Personal Statement Quality": {
            "Good": 60,
            "Average": 30,
            "Poor": 10
        }
    },
    {
        "Program": "BS (Accounting & Finance)",
        "Personal Statement Quality": {
            "Good": 25,
            "Average": 50,
            "Poor": 25
        }
    },
    {
        "Program": "BS (Computer Science)",
        "Personal Statement Quality": {
            "Good": 40,
            "Average": 35,
            "Poor": 25
        }
    },
    {
        "Program": "BS (Economics & Mathematics)",
        "Personal Statement Quality": {
            "Good": 35,
            "Average": 40,
            "Poor": 25
        }
    },
    {
        "Program": "BS (Economics)",
        "Personal Statement Quality": {
            "Good": 40,
            "Average": 30,
            "Poor": 30
        }
    },
    {
        "Program": "BS (Social Sciences)",
        "Personal Statement Quality": {
            "Good": 50,
            "Average": 40,
            "Poor": 10
        }
    },
    {
        "Program": "BS Mathematics",
        "Personal Statement Quality": {
            "Good": 20,
            "Average": 50,
            "Poor": 30
        }
    },
    # ... Add more bachelor programs data ...
]

# Sample data for master's programs
masters_data = [
     {
        "Program": "MBA Evening",
        "Personal Statement Quality": {
            "Good": 10,
            "Average": 25,
            "Poor": 65
        }
    },
    {
        "Program": "MBA Executive",
        "Personal Statement Quality": {
            "Good": 60,
            "Average": 25,
            "Poor": 15
        }
    },
    {
        "Program": "MBA Morning",
        "Personal Statement Quality": {
            "Good": 40,
            "Average": 20,
            "Poor": 40
        }
    },
    {
        "Program": "MS (Computer Science)",
        "Personal Statement Quality": {
            "Good": 60,
            "Average": 25,
            "Poor": 15
        }
    },
    {
        "Program": "MS (Economics)",
        "Personal Statement Quality": {
            "Good": 35,
            "Average": 40,
            "Poor": 25
        }
    },
    {
        "Program": "MS (Islamic Banking & Finance)",
        "Personal Statement Quality": {
            "Good": 25,
            "Average": 30,
            "Poor": 45
        }
    },
    {
        "Program": "MS (Marketing)",
        "Personal Statement Quality": {
            "Good": 15,
            "Average": 40,
            "Poor": 45
        }
    },
    {
        "Program": "MS (Mathematics)",
        "Personal Statement Quality": {
            "Good": 60,
            "Average": 25,
            "Poor": 15
        }
    },
    {
        "Program": "MS - Data Sciences",
        "Personal Statement Quality": {
            "Good": 40,
            "Average": 40,
            "Poor": 20
        }
    },
    {
        "Program": "MS - Development Studies",
        "Personal Statement Quality": {
            "Good": 50,
            "Average": 35,
            "Poor": 15
        }
    },
    {
        "Program": "MS - Finance",
        "Personal Statement Quality": {
            "Good": 20,
            "Average": 40,
            "Poor": 40
        }
    },
    {
        "Program": "MS - Management (Full Time)",
        "Personal Statement Quality": {
            "Good": 30,
            "Average": 30,
            "Poor": 40
        }
    },
    {
        "Program": "MS - Management (Part-Time)",
        "Personal Statement Quality": {
            "Good": 45,
            "Average": 35,
            "Poor": 20
        }
    }
    # ... Add more master's programs data ...
]

# Create stacked bar plot for a specific program
def create_program_bar_plot(program_data, title):
    qualities = list(program_data["Personal Statement Quality"].keys())
    values = list(program_data["Personal Statement Quality"].values())

    fig = go.Figure(data=[
        go.Bar(x=qualities, y=values)
    ])

    fig.update_layout(title=title)

    return fig


# Sidebar selection
selected_program_type = st.sidebar.radio("Select Program Type", ["Bachelor", "Master's"])

if selected_program_type == "Bachelor":
    selected_program = st.sidebar.selectbox("Select a Bachelor Program", [program["Program"] for program in bachelor_data])
    selected_program_data = next(program for program in bachelor_data if program["Program"] == selected_program)
else:
    selected_program = st.sidebar.selectbox("Select a Master's Program", [program["Program"] for program in masters_data])
    selected_program_data = next(program for program in masters_data if program["Program"] == selected_program)

# Create and display the selected program's plot
# Use Streamlit's layout capabilities to arrange plots side by side
col1, col2 = st.columns((4,8))
with col1:
    st.plotly_chart(create_program_bar_plot(selected_program_data, f"program selected {selected_program}"), use_container_width=True)
with col2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.write('Analyzing students personal statements, their emphasized backgrounds, and the chosen programs helps judge how well they match. When these aspects align well, its considered good. But if they dont match perfectly, its labeled as average or even poor, showing the need for clearer connections between their goals and qualifications.')
    # Create bullet points using Markdown syntax
    bullet_points = [
        "Good - Students backgrounds and requested programs are perfectly aligned in their personal statements.",
        "Average - Students' backgrounds don't perfectly match their requested programs in their personal statements.",
        "Poor - Students fail to mention their relevant experience or background for the program they want to enroll in their personal statements.",
    ]

    for bullet_point in bullet_points:
        st.markdown(f"- {bullet_point}")




############################################################################################################



# Sample data for bachelor programs
bachelor_data = [
    {
        "Program": "BBA",
        "Good": 60,
        "Average": 30,
        "Poor": 10
    },
    {
        "Program": "BS (Accounting & Finance)",
        "Good": 25,
        "Average": 50,
        "Poor": 25
    },
    {
        "Program": "BS (Computer Science)",
        "Good": 40,
        "Average": 35,
        "Poor": 25
    },
    {
        "Program": "BS (Economics & Mathematics)",
        "Good": 35,
        "Average": 40,
        "Poor": 25
    },
    {
        "Program": "BS (Economics)",
        "Good": 40,
        "Average": 30,
        "Poor": 30
    },
    {
        "Program": "BS (Social Sciences)",
        "Good": 50,
        "Average": 40,
        "Poor": 10
    },
    {
        "Program": "BS Mathematics",
        "Good": 20,
        "Average": 50,
        "Poor": 30
    }
    # ... Add more bachelor programs data here ...
]

# Sample data for master's programs
masters_data = [
        {
        "Program": "MS (Computer Science)",
        "Good": 60,
        "Average": 25,
        "Poor": 15
    },
    {
        "Program": "MS (Economics)",
        "Good": 35,
        "Average": 40,
        "Poor": 25
    },
    {
        "Program": "MS (Islamic Banking & Finance)",
        "Good": 25,
        "Average": 30,
        "Poor": 45
    },
    {
        "Program": "MS (Marketing)",
        "Good": 15,
        "Average": 40,
        "Poor": 45
    },
    {
        "Program": "MS (Mathematics)",
        "Good": 60,
        "Average": 25,
        "Poor": 15
    },
    {
        "Program": "MS - Data Sciences",
        "Good": 40,
        "Average": 40,
        "Poor": 20
    },
    {
        "Program": "MS - Development Studies",
        "Good": 50,
        "Average": 35,
        "Poor": 15
    },
    {
        "Program": "MS - Finance",
        "Good": 20,
        "Average": 40,
        "Poor": 40
    },
    {
        "Program": "MS - Management (Full Time)",
        "Good": 30,
        "Average": 30,
        "Poor": 40
    },
    {
        "Program": "MS - Management (Part-Time)",
        "Good": 45,
        "Average": 35,
        "Poor": 20
    }
    # ... Add more master's programs data here ...
]

# Create stacked bar plots for bachelor and master's programs
def create_stacked_bar_plot(data, title):
    programs = [item["Program"] for item in data]
    good_values = [item["Good"] for item in data]
    average_values = [item["Average"] for item in data]
    poor_values = [item["Poor"] for item in data]

    fig = go.Figure(data=[
        go.Bar(name='Good', x=programs, y=good_values),
        go.Bar(name='Average', x=programs, y=average_values),
        go.Bar(name='Poor', x=programs, y=poor_values)
    ])

    fig.update_layout(barmode='stack', title=title)

    return fig


# Create the bachelor and master's plots
bachelor_plot = create_stacked_bar_plot(bachelor_data, "Bachelor Programs")
masters_plot = create_stacked_bar_plot(masters_data, "Master's Programs")

# Use Streamlit's layout capabilities to arrange plots side by side
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(bachelor_plot, use_container_width=True)

with col2:
    st.plotly_chart(masters_plot, use_container_width=True)


# Display additional information if needed
# st.write("Additional information can be displayed here.")
