# Getting Started

1. Clone this repo.
    ```bash
    git clone https://github.com/titus-chin/rooms-for-rent-in-singapore
    ```

2. Navigate into project directory.
    ```bash
    cd rooms-for-rent-in-singapore
    ```

3. Create virtual environment. Note that the actual steps for creating virtual environment might vary for different operating systems. Commands below show how to create a virtual environment using pip and virtualenv in Linux.
    ```bash
    python3 -m pip install virtualenv
    virtualenv venv
    ```

4. Activate virtual environment and install dependencies. Note that the actual steps for activating virtual environment or installing dependencies might vary for different operating systems. Commands below show how to activate virtual environment and install dependencies using pip and virtualenv in Linux.
    ```bash
    source venv/bin/activate
    python3 -m pip install -r requirements.txt
    ```

5. Scrape rental lists from roomz.asia.
    ```bash
    python3 src/data/rental_scraper.py
    ```

6. Run streamlit app locally.
    ```bash
    streamlit run app.py
    ```