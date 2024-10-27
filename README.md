# GitHub-Jira Integration with Python and Flask

This project is a simple integration between GitHub and Jira, built with Python and Flask. It automates the process of logging GitHub issues in Jira, tracking commits against Jira issues, and syncing other data points between GitHub and Jira to streamline development workflows.

## Features

- **Create Jira Issues from GitHub**: Automatically create Jira issues based on GitHub events like issue creation or pull requests.
- **Sync GitHub Commits with Jira**: Link GitHub commits to Jira issues by referencing issue keys in commit messages.
- **Webhook Integration**: Uses GitHub webhooks to listen for relevant events and process them in real-time.

## Prerequisites

- **Python 3.6 or above**
- **Flask** web framework
- **Requests** library for making API calls
- Jira API access (Jira Cloud or Jira Server)
- GitHub account with permissions to set up webhooks

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pkpatil7057/Simple-flask-app
   cd Simple-flask-app
