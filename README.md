🚨 [KodamaChameleon.com](https://kodamachameleon.com) has not been updated yet and is still utilizing Word Press. This notice will come down once it has been converted.

# Webtile
**A Simple Markdown Website Content Manager**

<img src="/static/img/kodama.png" alt="kodama" width="300">

![Python](https://img.shields.io/badge/Python-3.10.12-blue.svg?logo=python) <!-- GEN:playwright-version-badge -->![Playwright](https://img.shields.io/badge/Flask-3.0.3-blue.svg?logo=Flask)<!-- GEN:stop -->

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to **Webtile**, a minimalistic and mobile-friendly blog and community platform built with Flask. Webtile allows you to showcase blog posts, feature articles, and community resources with ease.

## Features

- 📝 **Blog**: Create and manage blog posts written in Markdown.
- 🌟 **Featured Post**: Highlight a featured blog post on the main blog page.
- 🏘️ **Community**: List and describe various organizations and resources in a dedicated community page.
- 🌐 **Mobile-Friendly**: Responsive design for seamless usage on both desktop and mobile devices.
- 📂 **Markdown Support**: Write posts in Markdown and render them beautifully.
- 🔍 **Logging**: Comprehensive request and error logging.

## Installation

### Prerequisites

- Python 3.6+
- Flask

### Setup

1. **Clone the Repository**
 ```bash
 git clone https://github.com/yourusername/webtile.git
 cd webtile
 ```
2. **Create a Virtual Environment**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
3. **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```
4. **Set Environment Variables**
  Create a .env file and set your environment variables as required by the Environment class in scripts/utils.py.

## Usage

### Running the App Locally
```bash
python launch.py -h
usage: launch.py [-h] [-v] [-e ENVIRONMENT]

Launch the webtile flask application

options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose output for debugging
  -e ENVIRONMENT, --environment ENVIRONMENT
                        Environment file name (default: .env)
```

### Running with Gunicorn
For production environments:
```bash
gunicorn -w 4 -b 127.0.0.1:8000 launch:app
```

## Configuration
- **Logging**: Configure logging settings in .env
- **Featured Post**: Set the filename of the featured post in the environment variable FEATURED_POST.

## Contributing
Contributions are welcome! Please fork this repository and submit pull requests.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a pull request.

## License
![image](https://img.shields.io/badge/License-GNU%20GPL-blue)

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.fr.html)

---
Made with ❤️ by Kodama Chameleon
