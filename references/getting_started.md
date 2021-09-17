# Getting Started

1. Clone this repo.
    ```bash
    $ git clone https://github.com/titus-chin/rooms-for-rent-in-singapore
    ```

2. Navigate into project directory.
    ```bash
    $ cd rooms-for-rent-in-singapore
    ```

3. Create virtual environment. One can easily create one using pip and virtualenv.
    ```bash
    $ pip3 install virtualenv
    $ virtualenv venv
    ```

4. Install dependencies into virtual environment.
    ```bash
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```

5. Scrape rental lists from roomz.asia.
    ```bash
    $ python3 src/data/rental_scraper.py
    ```

6. Run streamlit app locally.
    ```bash
    $ streamlit run app.py
    ```