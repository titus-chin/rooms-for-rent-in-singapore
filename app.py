import boto3
import pandas as pd
import streamlit as st
from datetime import date
from pathlib import Path
from src.data.utils import load_config
import _thread


@st.cache(hash_funcs={_thread.RLock: id})
def load_data(date):
    """Load rental data to web app either from local machine or AWS S3
    bucket.

    Parameters
    ----------
    date : datetime.date
        Today's date to remove cached data daily.

    Returns
    -------
    pandas.DataFrame
    """
    try:
        client = boto3.client(
            "s3",
            aws_access_key_id=st.secrets["aws_access_key_id"],
            aws_secret_access_key=st.secrets["aws_secret_access_key"],
            region_name=st.secrets["region_name"],
        )
        obj = client.get_object(Bucket=st.secrets["bucket"], Key=st.secrets["key"])
        input_path = obj["Body"]
    except:
        input_path = f"{Path.cwd().joinpath('data', conf['input_file'])}"

    data = pd.read_csv(input_path)
    data.sort_values(conf["sort_by"], inplace=True)
    data.set_index(conf["index"], drop=True, inplace=True)
    return data


@st.cache
def get_location_options(data, area, date):
    """Get location options based on the area selected by users.

    Parameters
    ----------
    data : pandas.DataFrame
        Rental data.
    area : str
        Area where the rooms belong to.
    date : datetime.date
        Today's date to remove cached data daily.

    Returns
    -------
    numpy.ndarray or list
    """
    try:
        location = data.loc[area, "Location"].unique()
    except:
        location = [data.loc[area, "Location"]]
    return location


@st.cache
def select_data(data, area, location, date):
    """Return selected data based on users' choices.

    Parameters
    ----------
    data : pandas.DataFrame
        Rental data.
    area : str
        Area where the rooms belong to.
    location : list
        Location of the rooms.
    date : datetime.date
        Today's date to remove cached data daily.

    Returns
    -------
    pandas.DataFrame
    """
    selected_data = data.loc[area]
    try:
        selected_data = selected_data[selected_data["Location"].isin(location)]
    except:
        selected_data = pd.DataFrame(
            {
                "Location": location,
                f"Rent ({conf['currency']}/month)": selected_data.values[1],
                "Headline": selected_data.values[2],
                "Link": selected_data.values[3],
            }
        )
    return selected_data


if __name__ == "__main__":
    conf = load_config("conf", "parameters", "app.yaml")
    st.title(conf["title"])
    today_date = date.today()
    st.write(f"Updated at {today_date}")
    data_load_state = st.text("Loading data...")
    data = load_data(today_date)
    st.sidebar.markdown(
        conf["markdown"].format(
            conf["github"],
            conf["author"],
            conf["linkedin"],
        )
    )
    area = st.sidebar.radio("Select area:", options=set(data.index), index=0)
    location = st.sidebar.multiselect(
        "Select location:",
        options=get_location_options(data, area, today_date),
        default=get_location_options(data, area, today_date)[0],
    )
    selected_data = select_data(data, area, location, today_date)
    st.write(
        selected_data.to_html(escape=False, index=False, render_links=True),
        unsafe_allow_html=True,
    )
    data_load_state.text("Loading data...done!")
