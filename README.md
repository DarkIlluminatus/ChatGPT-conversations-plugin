# ChatGPT-conversations-plugin

[![License](https://img.shields.io/badge/license-GPL--3.0%20License%20with%20Additional%20Conditions-blue.svg)](LICENSE)

## Overview

This repository contains a plugin that enables ChatGPT to access previous conversations from a MongoDB database and provide context-aware responses based on the conversation history.

## Features

- Retrieve past conversations from a MongoDB database
- Provide context-aware responses based on conversation history
- Import conversation history from JSON and HTML files

## Installation

Clone the repository:

git clone https://github.com/DarkIlluminatus/ChatGPT-conversations-plugin.git


##Previous README.md for posterity:
#This repository is a WIP
The repository is not yet complete or functional, the below will soon be implemented. This work is essentially in pre-alpha status and this README will be modified accordingly as that status changes.

# ChatGPT-conversations-plugin
A plugin for ChatGPT that allows for context-aware responses using conversation history stored in a MongoDB database.

# ChatGPT Plugin for Conversation History

## License

This project is licensed under the GPL-3.0 License with Additional Conditions. See the [LICENSE](LICENSE) file for more details. The use of this product is limited to non-harmful, non-illegal, and non-proprietary purposes. It is intended to always be freely available and open source.


This repository contains a plugin that enables ChatGPT to access previous conversations from a MongoDB database and provide context-aware responses based on the conversation history.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [MongoDB Setup](#mongodb-setup)
- [Usage](#usage)
  - [Data Export and Import](#data-export-and-import)
    - [Data Export from ChatGPT](#data-export-from-chatgpt)
    - [Data Import to MongoDB](#data-import-to-mongodb)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieve past conversations from a MongoDB database
- Provide context-aware responses based on conversation history
- Import conversation history from JSON and HTML files

## Requirements

- Python 3.6 or higher
- MongoDB Community Edition
- MongoDB Compass (optional, for a graphical user interface)

## Installation

1. **Clone the repository:**
git clone https://github.com/DarkIlluminatus/ChatGPT-conversations-plugin.git

2. **Install Python dependencies:**
cd chatgpt-plugin
pip install -r requirements.txt

3. **Install MongoDB Community Edition:**
Follow the instructions [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) to install MongoDB on Windows.

4. **Set up MongoDB data directory:**
Choose the desired location for the data directory during the MongoDB installation process.

5. **Run MongoDB as a Windows service:**
Choose "Run service as Network Service user" during the installation process.

6. **(Optional) Install MongoDB Compass:**
Check the option to include Compass during the installation process.

## Data Export and Import

This section describes the process of exporting your ChatGPT conversation data, preparing the data for import, and importing it into your MongoDB database.

### Exporting Data from ChatGPT

1. Log in to your ChatGPT account.
2. Go to the Settings page.
3. Navigate to the Data Controls section.
4. Click on the "Export" button.
5. Your ChatGPT data will be emailed to the email address associated with your ChatGPT account.

### Preparing Data for Import

Once you receive the email with your ChatGPT data, download the attached files, which include the conversation data in JSON and HTML formats.

- Extract the conversation data from the JSON file using a JSON parser or a custom Python script.
- For the HTML file, you can use a Python library like Beautiful Soup to parse and extract the conversation data.

### Importing Data into MongoDB

With the conversation data prepared, you can now import it into your MongoDB database:

1. Create a new collection in your MongoDB database, e.g., `conversations`.
2. Use a script, MongoDB Compass, or the `mongoimport` command to import the conversation data into the `conversations` collection.

Please refer to the provided example scripts (once they are uploaded, of course) in this repository in /scripts/ folder for data extraction and import. Modify them as needed to suit your specific requirements.

## Usage

1. **Import conversation history:**
Modify the provided Python scripts to import your conversation history from JSON and HTML files into your MongoDB database.

2. **Create a text index:**
In MongoDB Compass or the MongoDB shell, create a text index on the `text` field of the `conversations` collection in your database.

3. **Start the ChatGPT plugin:**
python main.py


4. **Connect ChatGPT to the plugin:**
Follow the OpenAI API documentation on how to connect your ChatGPT instance to the plugin. (this step will be more detailed in the future)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to help improve the project.

1. Fork the repository
2. Create a new branch (`git checkout -b my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push the branch (`git push origin my-feature`)
5. Create a Pull Request

## License

This project is licensed under the GPL-3.0 License with Additional Conditions. See the [LICENSE](LICENSE) file for more details. The use of this product is limited to non-harmful, non-illegal, and non-proprietary purposes. It is intended to always be freely available and open source.
