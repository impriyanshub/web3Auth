# Caching System Testing Project

This project aims to test the functionality and performance of a caching system using Python and Django. The tests evaluate the caching system's behavior and its impact on response times.

## Getting Started

Follow these steps to set up and run the caching system testing project on your local machine.

### Prerequisites

- Python 3.9
- `pipenv` for managing virtual environments (if not already installed)
- Memcached (will be installed and configured as part of the setup process)

### Installation

1. **Clone the Repository:**

   Clone this repository to your local machine using Git:

   ```sh
   git clone https://github.com/impriyanshub/web3Auth.git
   cd web3Auth
   ```

2. **Install `pipenv`:**

   If you don't have `pipenv` installed, you can do so using the following command:

   ```sh
   pip install pipenv
   ```

3. **Install Dependencies:**

   Inside the project directory, use `pipenv` to install all project dependencies:

   ```sh
   pipenv install
   ```

4. **Install Memcached:**

   Depending on your operating system, follow the appropriate steps to install Memcached:

   - **Windows:**
     Download the Windows binary from the Memcached website (https://memcached.org/downloads) and start the `memcached.exe` service.

   - **Linux (Ubuntu):**
     Install Memcached using your package manager:

     ```sh
     sudo apt-get install memcached
     ```

   - **macOS (Homebrew):**
     Install Memcached using Homebrew:

     ```sh
     brew install memcached
     ```

5. **Start Memcached Server:**

   Start the Memcached server on port 11211. The caching system will use this server for caching data:

   ```sh
   memcached -p 11211
   ```

6. **Run Django Dev Server:**

   Start the Django development server on port 8000:

   ```sh
   cd web3Auth_project/
   python manage.py runserver 8000
   ```

7. **Access the Cached API:**

   Open your web browser and navigate to `http://localhost:8000/api/test`. You will see a page displaying the current timestamp. Upon refreshing the page, you will observe that the timestamp remains the same for 10 seconds before updating. This demonstrates the caching behavior.

8. **View the Code:**

   To view the code responsible for the caching behavior, open `web3Auth_project/app1/views.py`. The `@method_decorator(cache_page(10))` decorator controls the caching duration.

9. **Reconfigure Caching:**

   To change the caching duration, modify the `10` inside the `@method_decorator(cache_page(10))` decorator to your desired caching time in seconds.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
